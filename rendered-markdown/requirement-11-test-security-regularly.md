# Requirement 11 - Test Security of Systems and Networks Regularly
## Introduction

Requirement 11 ensures that systems and networks are tested proactively to identify vulnerabilities and unauthorized activities before they can be exploited. PCI DSS v4.0 strengthens expectations around penetration testing, vulnerability management, rogue wireless detection, and file integrity monitoring.

## Requirement 11 at a Glance

- Perform internal and external vulnerability scans.
- Conduct penetration tests simulating real-world attack paths.
- Detect and respond to unauthorized wireless access points.
- Deploy and monitor change detection mechanisms (FIM) on critical systems.

## What This Means in Practice

Organizations must regularly scan and test their environments for vulnerabilities, simulate real-world attacks through penetration testing, actively scan for rogue wireless devices, and monitor critical file changes. Mature programs integrate continuous scanning, automated alerting, and threat-informed penetration testing scenarios.

## Gotchas

- Failing to remediate critical vulnerabilities identified in scans.
- Penetration tests that don't reflect real-world threat scenarios.
- Ignoring wireless scans or only scanning limited locations.
- Change detection tools generating noise instead of actionable alerts.

## Trusted Advisor (TA) Tip

Move toward continuous vulnerability scanning models and conduct scenario-based penetration tests aligned with current threat intelligence. Integrate FIM alerts into SIEM workflows with risk-based prioritization to focus on critical file changes.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| 11.3.1 | Security Testing Team | CISO | Infrastructure and Application Owners | Compliance Officer |

## Use Case Lenses

**Executive Lens**

Demonstrates resilience against evolving cyber threats through proactive vulnerability and threat detection practices.

**Security & Infra Teams Lens**

Focuses on identifying weaknesses before attackers do, validating controls through pen testing, and monitoring critical changes proactively.

**QSA/Consultant Lens**

Look for vulnerability scan reports, penetration test scopes and results, rogue wireless detection processes, and evidence of file integrity monitoring.

**Small Business Lens**

Use managed scanning services, partner with external penetration testers, and adopt lightweight FIM tools tailored for small environments.

## Call to Action (CTA)

Review your vulnerability management, penetration testing, wireless scanning, and file monitoring processes today. Ensure findings are prioritized, remediated, and validated consistently.

