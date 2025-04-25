# Requirement 4 - Protect Cardholder Data with Strong Cryptography During Transmission
## Introduction

Requirement 4 ensures that sensitive cardholder data is protected during transmission over open, public networks. PCI DSS v4.0 strengthens expectations around the use of strong cryptographic protocols, inventory tracking of transmission methods, and validation of encryption failure scenarios.

## Requirement 4 at a Glance

- Encrypt all cardholder data transmitted over open/public networks.
- Use strong cryptography (TLS 1.2+, SSH, IPsec).
- Disable SSL, early TLS, and weak protocols.
- Maintain inventories of data transmission paths.
- Validate encryption controls regularly.

## What This Means in Practice

Organizations must encrypt all sensitive cardholder data transmissions using strong protocols, monitor and disable outdated methods, maintain inventories of where sensitive data travels, and ensure encryption failure detection mechanisms are in place. Mature environments also automate inventory and certificate lifecycle management.

## Gotchas

- Forgotten legacy systems still allowing SSL/TLS 1.0 fallback.
- APIs using plain HTTP or insecure WebSocket.
- No active monitoring of cert expiration.
- VPN tunnels without enforced encryption policies.
- Gaps in transmission inventories.

## Trusted Advisor (TA) Tip

Build an automated inventory that tracks every endpoint and service transmitting cardholder data. Integrate SSL/TLS scanning tools into your asset management workflows to detect insecure endpoints automatically.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| 4.1.1 | Network Security Team | Security Operations Manager | Application Developers | Compliance Officer |

## Use Case Lenses

**Executive Lens**

Encryption protects customer trust and reduces breach impact if data interception occurs.

**Security & Infra Teams Lens**

Requires active monitoring of encryption health, inventory maintenance, and swift remediation of insecure paths.

**QSA/Consultant Lens**

Look for proof of strong encryption on all open/public transmissions, inventories of transmission paths, and evidence of deprecated protocol disabling.

**Small Business Lens**

Use cloud services that handle encryption automatically, and validate endpoint security settings through routine external scans.

## Call to Action (CTA)

Review your system inventories and confirm that all sensitive transmissions are secured with strong cryptography. Schedule regular scans for insecure protocols.

