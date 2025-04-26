# Requirement 2 - Apply Secure Configurations to All System Components
## Introduction

Requirement 2 ensures that all system components are securely configured to prevent exploitation of default settings. PCI DSS v4.0 expands the need for secure cloud, container, and serverless environments.

## Requirement 2 at a Glance

- Change default passwords.
- Harden configurations using industry standards.
- Maintain documented baselines.
- Extend to cloud and mobile environments.

## What This Means in Practice

Organizations should use hardened images, change all vendor defaults, and continuously validate configurations. Maturity means automating hardening checks and scanning new assets at onboarding.

## Gotchas

- Default accounts disabled but not removed.
- Missing hardening for cloud and serverless services.
- No documentation of security configurations.

## Trusted Advisor (TA) Tip

Automate baseline configuration scans and integrate secure config validation into CI/CD pipelines.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| 2.2.1 | Sysadmins | Infrastructure Manager | Security Architect | Compliance Officer |

## Use Case Lenses

**Executive Lens**

Reduces breach risk by eliminating simple entry points.

**Security & Infra Teams Lens**

Focuses on standardizing and validating secure builds.

**QSA/Consultant Lens**

Look for documented baselines and hardened images.

**Small Business Lens**

Use vendor-hardened templates and change defaults during setup.

## Call to Action (CTA)

Assess your environment today: verify that all deployed systems follow a secure baseline.

