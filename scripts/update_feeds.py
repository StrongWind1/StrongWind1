#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Refresh the activity feeds in the profile README.

Replaces content between HTML comment markers (`<!-- foo_start -->` /
`<!-- foo_end -->`) with the latest items from each source. Runs on a cron
from `.github/workflows/feeds.yml` and commits any diff back to the repo.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

USER = "StrongWind1"
README = Path("README.md")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# The "Protocol analysis" column is a curated list of reference-doc repos,
# rendered with their live description and star count.
ANALYSIS_REPOS = ("Kerberos", "WiFi_Cracking")

MAX_ITEMS = 5
# Over-fetch per repo so draft releases can't crowd out published ones before the global top-MAX_ITEMS cut.
RELEASES_PER_REPO = 10
HTTP_TIMEOUT = 30
DESC_MAX = 70
DESC_TRUNC = 67


def gh_api(path: str) -> list | dict:
    """Call the GitHub REST API and return parsed JSON."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-readme-updater",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as r:  # noqa: S310
        return json.load(r)


def owned_repos() -> list[str]:
    """Names of every non-fork repository owned by USER.

    Drives the release feed dynamically so a newly published tool appears
    without anyone editing this script.
    """
    try:
        repos = gh_api(f"/users/{USER}/repos?per_page=100&type=owner&sort=updated")
    except (urllib.error.URLError, KeyError, TypeError):
        return []
    if not isinstance(repos, list):
        return []
    names: list[str] = []
    for r in repos:
        if isinstance(r, dict) and not r.get("fork", False):
            name = r.get("name")
            if isinstance(name, str):
                names.append(name)
    return names


def _repo_releases(repo: str) -> list[tuple[str, str, str, str]]:
    """Published (non-draft) releases for one repo as (published_at, repo, name, url) tuples."""
    try:
        releases = gh_api(f"/repos/{USER}/{repo}/releases?per_page={RELEASES_PER_REPO}")
    except (urllib.error.URLError, KeyError, TypeError):
        return []
    if not isinstance(releases, list):
        return []
    out: list[tuple[str, str, str, str]] = []
    for rel in releases:
        if not isinstance(rel, dict) or rel.get("draft"):
            continue
        published = rel.get("published_at")
        if not isinstance(published, str) or not published:
            continue
        name = rel.get("name") or rel.get("tag_name") or ""
        url = rel.get("html_url") or ""
        out.append((published, repo, str(name), str(url)))
    return out


def fetch_releases() -> list[str]:
    """Latest published releases across every non-fork repo you own.

    Repos are discovered at runtime (see owned_repos), so shipping a release in
    any owned repo surfaces it here automatically. Drafts have no published_at
    and are skipped.
    """
    items: list[tuple[str, str, str, str]] = []
    for repo in owned_repos():
        items.extend(_repo_releases(repo))
    items.sort(reverse=True)
    if not items:
        return ["_No releases yet._"]
    return [f"- [{repo} · {name}]({url}) — {date[:10]}" for date, repo, name, url in items[:MAX_ITEMS]]


def fetch_analysis() -> list[str]:
    """List of protocol-analysis reference repos with current description and star count."""
    items: list[str] = []
    for repo in ANALYSIS_REPOS:
        try:
            r = gh_api(f"/repos/{USER}/{repo}")
        except (urllib.error.URLError, KeyError, TypeError):
            continue
        if not isinstance(r, dict):
            continue
        desc = (r.get("description") or "").strip()
        if len(desc) > DESC_MAX:
            desc = desc[:DESC_TRUNC] + "..."
        url = r.get("html_url", f"https://github.com/{USER}/{repo}")
        stars = r.get("stargazers_count", 0)
        items.append(f"- [**{repo}**]({url}) — {desc} · ★ {stars}")
    return items or ["_No analysis repos._"]


def replace_block(text: str, marker: str, body: str) -> str:
    """Swap content between `<!-- marker_start -->` / `<!-- marker_end -->`."""
    pattern = re.compile(
        rf"(<!-- {marker}_start -->).*?(<!-- {marker}_end -->)",
        flags=re.DOTALL,
    )
    return pattern.sub(rf"\1\n{body}\n\2", text)


def main() -> int:
    """Refresh every feed block in README.md."""
    feeds: dict[str, Callable[[], list[str]]] = {
        "releases": fetch_releases,
        "analysis": fetch_analysis,
    }
    text = README.read_text()
    for marker, fetcher in feeds.items():
        text = replace_block(text, marker, "\n".join(fetcher()))
    README.write_text(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
