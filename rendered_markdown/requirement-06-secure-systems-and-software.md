# Requirement 6 - Develop and Maintain Secure Systems and Software
## Introduction

Requirement 6 focuses on ensuring all systems and software are developed and maintained securely. PCI DSS v4.0 strengthens expectations around secure coding, software lifecycle management, vulnerability patching, and controlling third-party scripts in payment environments.

## Requirement 6 at a Glance

- Apply secure coding practices.
- Inventory and control third-party scripts.
- Patch vulnerabilities promptly.
- Maintain secure system configurations.
- Implement structured change control procedures.

## What This Means in Practice

Organizations must adopt secure software development lifecycles (SDLCs), scan applications for vulnerabilities before release, patch known vulnerabilities within vendor timelines, manage third-party scripts in payment pages, and apply formal change controls to all system changes.

## Gotchas

- Allowing unmanaged third-party scripts on payment pages.
- Neglecting to scan for vulnerabilities before production deployment.
- Deploying changes without formal approval or rollback plans.
- No documented secure coding standards for developers.

## Trusted Advisor (TA) Tip

Integrate static and dynamic application security testing (SAST/DAST) directly into your CI/CD pipelines. Require all third-party scripts in payment environments to undergo review and explicit authorization, and keep an inventory with update schedules.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| 6.4.3 | Application Security Team | Product Owners | Compliance | Operations and Release Managers |

## Use Case Lenses

**Executive Lens**

Protects the organization's reputation by minimizing the likelihood of breaches caused by code vulnerabilities or script misuse.

**Security & Infra Teams Lens**

Focuses on embedding security into development workflows, securing configurations, patching vulnerabilities, and reviewing third-party content.

**QSA/Consultant Lens**

Look for documented secure coding standards, software testing results, change control records, and script management evidence for payment environments.

**Small Business Lens**

Leverage cloud hosting and managed code scanning services, and maintain strict control over what scripts run on your e-commerce or payment pages.

## Call to Action (CTA)

Review your secure coding policies, change control processes, and inventory of third-party scripts today. Validate that application and infrastructure vulnerabilities are identified and patched within vendor-recommended timelines.

