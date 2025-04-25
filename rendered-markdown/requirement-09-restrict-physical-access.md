# Requirement 9 - Restrict Physical Access to Cardholder Data
## Introduction

Requirement 9 ensures that physical access to systems and environments handling cardholder data is tightly controlled. PCI DSS v4.0 strengthens expectations around visitor tracking, access control reviews, and integration of physical security monitoring with overall security systems.

## Requirement 9 at a Glance

- Restrict physical access to systems and data.
- Use ID badges, biometric readers, or equivalent controls.
- Maintain detailed visitor logs.
- Escort all visitors at all times.
- Review and revoke physical access rights regularly.

## What This Means in Practice

Organizations must deploy physical access control measures at all sensitive areas, track all visitors, review access lists regularly, and monitor access attempts. Mature programs integrate physical access data into centralized security monitoring and enforce strict separation of duties for access approvals.

## Gotchas

- Shared or propped-open doors.
- Visitor logs missing critical data (e.g., time of departure).
- Failure to revoke access after role or employment changes.
- Security cameras not covering all entry and sensitive points.

## Trusted Advisor (TA) Tip

Integrate badge access logs and visitor management systems with SIEM or centralized security monitoring to enable near real-time detection of unauthorized access attempts. Regularly audit surveillance footage to confirm that visitor escort policies are being followed.

## RACI Matrix for Key Sub-Requirements

| Sub-Requirement | Responsible | Accountable | Consulted | Informed |
|:----------------|:------------|:-----------|:----------|:--------|
| 9.4.1 | Facilities Security Team | Facilities Manager | Compliance Officer | HR and IT Security |

## Use Case Lenses

**Executive Lens**

Reduces insider threats and strengthens overall security posture, protecting organizational reputation and customer trust.

**Security & Infra Teams Lens**

Focuses on maintaining secure physical perimeters, access monitoring, visitor management, and physical access audits.

**QSA/Consultant Lens**

Look for evidence of physical access reviews, visitor logs, access control lists, and proof that no individual approves their own physical access rights.

**Small Business Lens**

Use simple electronic access badge systems with enforced visitor sign-ins and escort policies.

## Call to Action (CTA)

Conduct a physical access audit today. Validate that all access controls are operating correctly, visitor policies are enforced, and that access rights are revoked promptly when no longer needed.

