<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=220&section=header&text=StrongWind&fontSize=84&fontColor=ffffff&fontAlignY=38&animation=fadeIn&desc=Windows%20%2F%20Active%20Directory%20and%20Wi-Fi%20Security%20Research&descSize=18&descAlignY=62&descColor=cfd8dc" alt="StrongWind" />

</div>

I build spec-accurate offensive security tooling for Active Directory, Kerberos, and Wi-Fi — Python and Rust, validated against the wire, not guessed.

## Contact

[hello@strongwind.dev](mailto:hello@strongwind.dev) &bull; [@StrongWind@infosec.exchange](https://infosec.exchange/@StrongWind) &bull; [@Strong1Wind](https://x.com/Strong1Wind) &bull; [u/StrongWind1](https://reddit.com/user/StrongWind1/)

## Tools

| Tool | Purpose | Lang |
| --- | --- | --- |
| [**CredWolf**](https://github.com/StrongWind1/CredWolf) | Validate AD credentials over NTLM and Kerberos — passwords, hashes, keys, tickets | Python |
| [**KerbWolf**](https://github.com/StrongWind1/KerbWolf) | Kerberos roasting and TGT attack toolkit for Active Directory | Python |
| [**NTDSWolf**](https://github.com/StrongWind1/NTDSWolf) | Offline NTDS.dit parser and credential extractor — NT/LM, Kerberos keys, LAPS, gMSA | Python |
| [**AD-SecretGen**](https://github.com/StrongWind1/AD-SecretGen) | Derive every password-derived AD secret (NT/LM, Kerberos keys, WDigest) from a password | Python |
| [**NFSWolf**](https://github.com/StrongWind1/NFSWolf) | Native NFSv2/v3/v4 recon, enumeration, exploitation, and interactive shell | Rust |
| [**WPAWolf**](https://github.com/StrongWind1/WPAWolf) | WPA / WPA2 / WPA3-FT-PSK handshake extractor for hashcat (modes 22000 + 37100) | Rust |

> **Currently researching:**
>
> - new Kerberos abuse primitives in KerbWolf
> - deeper WPA/WPA2 PSK analysis with WPAWolf
> - folding public NFS vulnerabilities into NFSWolf as a single fast, statically-linked binary

## Reference docs

- [**Kerberos**](https://github.com/StrongWind1/Kerberos) — protocol internals, security configuration, and attack techniques in MS Active Directory
- [**WiFi_Cracking**](https://github.com/StrongWind1/WiFi_Cracking) — WPA / WPA2 PSK security analysis reference

## Recent activity

<table>
<tr>
<td valign="top" width="50%">

### Tool releases

<!-- releases_start -->
- [WPAWolf · v1.1.0](https://github.com/StrongWind1/WPAWolf/releases/tag/v1.1.0) — 2026-06-24
- [WPAWolf · v1.0.0](https://github.com/StrongWind1/WPAWolf/releases/tag/v1.0.0) — 2026-06-23
- [WEPWolf · v1.0.0](https://github.com/StrongWind1/WEPWolf/releases/tag/v1.0.0) — 2026-06-17
- [NFSWolf · v0.3.1](https://github.com/StrongWind1/NFSWolf/releases/tag/v0.3.1) — 2026-06-16
- [WEPWolf · v0.1.0](https://github.com/StrongWind1/WEPWolf/releases/tag/v0.1.0) — 2026-06-16
<!-- releases_end -->

</td>
<td valign="top" width="50%">

### Protocol analysis

<!-- analysis_start -->
- [**Kerberos**](https://github.com/StrongWind1/Kerberos) — Comprehensive reference for Kerberos authentication in Microsoft Ac... · ★ 7
- [**WiFi_Cracking**](https://github.com/StrongWind1/WiFi_Cracking) — Complete technical reference for WPA/WPA2 PSK security analysis · ★ 2
<!-- analysis_end -->

</td>
</tr>
</table>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=120&section=footer" alt="" />

</div>
