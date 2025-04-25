# Requirement 1 - Install and Maintain Network Security Controls
## Introduction

Requirement 1 lays the foundation for PCI DSS compliance by establishing network security controls at the perimeter and internally. PCI DSS v4.0 adds flexibility for custom approaches, provided control objectives are met.

## Requirement 1 at a Glance

- Build secure network boundaries.
- Control inbound and outbound traffic.
- Review ports, protocols, and services regularly.
- Justify each connection's business need.
- Protect against unauthorized network access, including cloud and virtual segmentation.

## What This Means in Practice

Businesses must implement firewalls or equivalent controls, document business justifications, and regularly review network access paths. Minimum compliance means having static firewalls with yearly reviews; maturity includes automated change detection.

## Gotchas

- Leaving cloud security groups unreviewed.
- Unused interfaces left open.
- Scoping errors from outdated network diagrams.

## Trusted Advisor (TA) Tip

Treat cloud VPCs and security groups with the same rigor as firewalls. Build automated alerting for unauthorized network changes.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| 1.2.5 | Network Security | CISO | Compliance | IT Operations |

## Use Case Lenses

**Executive Lens**

Supports business resilience and protects brand reputation.

**Security & Infra Teams Lens**

Focuses on least privilege and traffic restrictions.

**QSA/Consultant Lens**

Look for up-to-date diagrams, firewall configs, and rule justifications.

**Small Business Lens**

Use managed firewall services and document access rules carefully.

## Call to Action (CTA)

Review your firewall rules and cloud security groups today for scope alignment.

