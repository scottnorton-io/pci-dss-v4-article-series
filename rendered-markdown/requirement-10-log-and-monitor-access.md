# Requirement 10 - Log and Monitor All Access to System Components and Cardholder Data
## Introduction

Requirement 10 focuses on logging and monitoring access to all system components and cardholder data. PCI DSS v4.0 strengthens expectations for automated event detection, consistent log review practices, time synchronization, and log protection to ensure security events are detected and addressed promptly.

## Requirement 10 at a Glance

- Capture and store logs for all access and activity.
- Implement daily log reviews for critical systems.
- Use secure, authenticated time sources.
- Protect logs from unauthorized changes.
- Retain logs securely for forensic and incident response use.

## What This Means in Practice

Organizations must capture detailed logs from systems that store, process, or transmit cardholder data, review critical logs daily, ensure clocks are synchronized, prevent unauthorized modifications of logs, and retain log data securely for analysis. Mature organizations use centralized SIEM systems with automated alerting on suspicious events.

## Gotchas

- Inconsistent daily review of security event logs.
- Log files stored locally without centralization.
- System clocks drifting and causing inconsistent log timelines.
- No access controls preventing log tampering by administrators.

## Trusted Advisor (TA) Tip

Deploy a SIEM solution that not only centralizes log collection but also automates detection of suspicious patterns. Integrate time source health checks into your monitoring strategy to prevent unnoticed drift.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| 10.4.1 | Security Operations Center (SOC) | CISO | System Administrators | Compliance Officer |

## Use Case Lenses

**Executive Lens**

Reduces breach impact by enabling early detection of security incidents and demonstrating proactive governance.

**Security & Infra Teams Lens**

Focuses on capturing comprehensive logs, daily review routines, real-time alerting, and ensuring time source integrity.

**QSA/Consultant Lens**

Look for evidence of log collection from all critical assets, daily review documentation, tamper protection, and time synchronization validation.

**Small Business Lens**

Use managed SIEM or cloud-based logging services to meet centralized logging and monitoring requirements efficiently.

## Call to Action (CTA)

Review your logging and monitoring today. Confirm that logs are centrally collected, daily reviews are happening, time sources are authenticated, and logs are securely retained for at least 12 months.

