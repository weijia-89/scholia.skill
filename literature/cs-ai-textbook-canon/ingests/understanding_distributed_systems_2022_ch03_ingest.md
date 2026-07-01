# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 3

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch03_ingest.md |
| text_lines_read | 979–1153 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| chapter_number | 3 |
| chapter_title | Secure links |
| page_range | [not in text export] |

---

## Scope

Chapter 3 layers **TLS** on TCP to protect bytes in transit. TLS provides **encryption** (asymmetric key exchange → symmetric bulk encryption, periodic renegotiation), **authentication** (digital signatures, certificate chains, CAs, trust stores), **integrity** (HMAC beyond TCP checksum weakness), and the **handshake** (cipher suite negotiation, shared secret, server cert verification; TLS 1.2 ≈2 RTT, TLS 1.3 ≈1 RTT). Operational emphasis: use TLS everywhere; automate cert renewal to avoid expiry outages.

---

## Key findings

1. **TLS role** (lines 983–990): Runs on TCP; obfuscates channel for HTTP (HTTPS). Three guarantees: encryption, authentication, integrity.

2. **Encryption** (§3.1, lines 993–1021): Initial **asymmetric** exchange creates shared secret never sent on wire (elliptic-curve math). Then fast **symmetric** encryption for bulk data; shared key periodically renegotiated. CPU cost negligible on modern hardware with crypto instructions → **TLS for all communications**, including internal.

3. **Authentication** (§3.2, lines 1024–1092): Server signs messages with private key; client verifies with public key. Public key authenticity via **certificates** (entity, expiry, public key, issuer signature). **Certificate chain** ends at self-signed **root CA** (Figure 3.1). Client trust store must contain chain ancestor. Chain sent server→client on connect; reverse verification from trusted anchor. **Common failure:** expired certificates → connection failures → automate monitor/renew (Let's Encrypt cited).

4. **Integrity** (§3.3, lines 1095–1122): Middleman could tamper even if encrypted. TLS **HMAC** (secure hash) detects tampering/corruption. TCP checksum alone unreliable (~1 error per 16 GB–10 TB for 1 KB packets per cited study).

5. **Handshake** (§3.4, lines 1125–1153): Negotiate **cipher suite** (key exchange, signature, symmetric cipher, HMAC algorithms); create shared secret; verify server cert (optional client cert). Order optimized in modern stacks. New connection cost → geographic proximity + connection reuse (recurring Part I theme).

---

## Pedagogy

### Learning objectives

1. Name TLS's three guarantees and how they map to attack types.
2. Contrast asymmetric vs. symmetric encryption usage in TLS.
3. Explain certificate chain verification and expiry risk.
4. Articulate why HMAC supplements TCP checksums.
5. Compare TLS 1.2 vs. 1.3 handshake RTT cost.

### worked_examples_present

**Y** — Certificate chain diagram (Figure 3.1); handshake step list. No coding lab.

### exercise_hooks

1. Runbook: cert expiry monitoring checklist.
2. Trace a TLS failure from browser error to root cause class (expiry vs. untrusted CA vs. hostname mismatch).

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.3 §3.1–3.4 | Read | lines 979–1153 |
| Ch.4+ | Deferred | line 1154 onward |

---

## Operator hooks

Pairs with **DDIA** security discussion and production **AI Engineering** deployments (API keys in transit). Cert expiry as classic unknown-unknowns outage class (Ousterhout Ch.2 lens).

---

## TEXTBOOK-Q1 verdict

**PASS** — RFC 8446, operational guidance, clear procedural content.

---

## Glossary

| Term | Definition |
|------|------------|
| TLS | Transport Layer Security on TCP |
| CA | Certificate authority issuing signed certificates |
| HMAC | Keyed hash for message authentication |
| Cipher suite | Agreed algorithms for secure channel |
