# Requirement 3 - Protect Stored Account Data
## Introduction

Requirement 3 focuses on protecting stored cardholder data and sensitive authentication data. PCI DSS v4.0 strengthens expectations around encryption, tokenization, retention minimization, and access control to ensure stored data does not become an easy target for attackers.

## Requirement 3 at a Glance

- Encrypt stored PAN using strong cryptography.
- Implement robust key management processes.
- Mask PAN when displayed.
- Delete stored account data when no longer needed.
- Confirm tokenized data is truly out of scope if applicable.

## What This Means in Practice

Organizations should encrypt all stored PAN, properly manage encryption keys, mask account numbers where feasible, and delete data that is no longer needed. Mature programs simulate encryption failure scenarios and conduct frequent data discovery scans.

## Gotchas

- PAN accidentally stored in debug logs, snapshots, backups, or CDN caches.
- Poor key management practices or expired keys still in use.
- Assuming tokenized data is always out of PCI scope without validating irreversibility.
- Masking user displays but retaining full PANs in databases.

## Trusted Advisor (TA) Tip

Regularly scan your environments—including backups, logs, and third-party services—for residual PAN. Validate tokenization processes annually. Test failover scenarios to verify that encryption or tokenization failures are detected and remediated promptly.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| 3.4.1 | Data Protection Team | CISO | Database Administrators | Compliance Officer |

## Use Case Lenses

**Executive Lens**

Demonstrates risk management maturity by protecting high-value sensitive data and limiting breach impact.

**Security & Infra Teams Lens**

Demands strict encryption practices, key lifecycle management, and sensitive data discovery processes.

**QSA/Consultant Lens**

Look for documented encryption methods, key management evidence, and validation that masking is correctly enforced at display points.

**Small Business Lens**

Use built-in encryption services and limit storage.

## Call to Action (CTA)

Perform a sensitive data discovery scan today. Verify that all stored PAN is encrypted, masked where appropriate, and that key management processes are clearly documented and followed.

