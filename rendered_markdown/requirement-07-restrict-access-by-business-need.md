# Requirement 7 - Restrict Access to System Components and Cardholder Data by Business Need to Know
## Introduction

Requirement 7 ensures that access to systems and cardholder data is granted strictly based on business need to know. PCI DSS v4.0 enhances requirements around role-based access control, separation of duties, and periodic access reviews to reduce the risk of unauthorized access.

## Requirement 7 at a Glance

- Implement access control based on least privilege.
- Enforce role-based access or equivalent.
- Separate duties so no one can approve and grant their own access.
- Perform periodic access reviews and validations.

## What This Means in Practice

Organizations must define roles with minimal access privileges, enforce approval workflows for access grants, ensure that no individual can both approve and provision access for themselves, and regularly audit user access rights. Mature organizations dynamically adjust access based on changes in roles or employment status.

## Gotchas

- Administrators retaining excessive privileges over time.
- Failure to separate access approvers from access implementers.
- Infrequent or poorly documented access reviews.
- Terminated users retaining lingering access rights.

## Trusted Advisor (TA) Tip

Integrate identity governance tools that automate access provisioning and certification. Risk-rank user accounts during periodic reviews to prioritize high-privilege and sensitive access validation first.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| 7.2.1 | Access Management Team | IT Security Manager | HR and Department Managers | Compliance Team |

## Use Case Lenses

**Executive Lens**

Mitigates risk of insider threats and enhances trust with customers and auditors.

**Security & Infra Teams Lens**

Focuses on maintaining least privilege, automating access reviews, and implementing strong separation of duties.

**QSA/Consultant Lens**

Look for documented role definitions, access grant approvals, evidence of access reviews, and proof of separation of access approval and implementation.

**Small Business Lens**

Use simple RBAC templates, enforce access request approval chains, and schedule quarterly manual access reviews.

## Call to Action (CTA)

Review your access control policies today. Validate that access approvals require separate individuals for request and implementation, and schedule your next periodic access review.

