# Appendix A1 and A2 - Shared Hosting Providers and SSL/Early TLS for POI Systems
## Introduction

Appendices A1 and A2 of PCI DSS v4.0 address specialized environments requiring additional controls. A1 targets shared hosting providers who must ensure customer environments remain isolated and secure. A2 applies to organizations using SSL or early TLS in legacy point-of-sale (POI) systems, requiring strong compensating controls and formal risk management.

## Appendix A1 and A2 at a Glance

- Appendix A1: Enforce strict logical separation between shared hosting customers.
- Appendix A1: Maintain customer-specific logging and security control isolation.
- Appendix A2: Permit SSL/early TLS use in legacy POI systems only with risk mitigation and migration plans.
- Appendix A2: Verify devices are not susceptible to known vulnerabilities.

## What This Means in Practice

Shared hosting providers must enforce rigorous logical segmentation and independent security controls per customer. Organizations using legacy POI devices with SSL/early TLS must document formal risk analyses, validate security posture against known vulnerabilities, and maintain active migration plans to stronger protocols.

## Gotchas

- Weak or misconfigured segmentation exposing hosted customer environments.
- Inadequate logging and audit trails per customer.
- Legacy POI devices running SSL without documented risk justification.
- No clear migration timelines away from weak protocols.

## Trusted Advisor (TA) Tip

For shared hosting: require independent security audits demonstrating customer isolation. For legacy POI: document every device using SSL/early TLS, monitor device firmware and patching status rigorously, and prioritize migration readiness assessments.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| A1.2 | Hosting Provider Infrastructure Team | Hosting Provider Security Officer | Compliance Officer | Customer Security Liaisons |
| A2.1 | POS Support Teams | CISO | Risk Management | Compliance and Legal |

## Use Case Lenses

**Executive Lens**

Demonstrates risk containment and forward-looking security management for legacy and shared environments.

**Security & Infra Teams Lens**

Focuses on isolating tenant environments in shared hosting and managing SSL/early TLS risk exposure in payment flows.

**QSA/Consultant Lens**

Look for segmentation test results, customer-specific controls documentation, SSL/early TLS risk assessments, and active migration project plans.

**Small Business Lens**

Use managed hosting providers that independently validate PCI DSS compliance. For POI, phase out legacy devices aggressively or mitigate using tokenization and point-to-point encryption (P2PE).

## Call to Action (CTA)

Shared hosting providers: schedule segmentation audits. POI system operators: document all SSL/early TLS devices, validate current risk postures, and update your migration timelines.

