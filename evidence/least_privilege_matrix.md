# Least-Privilege Matrix

## Overview
This matrix defines access by role to reduce unauthorized access, privilege escalation, and lateral movement.

| Role | Alerts | Logs | SOC Dashboard | Jump Host | Customer Records DB | Model Config | Policy Docs |
|---|---|---|---|---|---|---|---|
| SOC Analyst | Read | Read | Read/Update case status | No Access | No Access | No Access | Read |
| Senior Analyst | Read | Read | Read/Update | Restricted Approval-Based | No Access | No Access | Read |
| SOC Engineer | Read | Read | Admin Support | Restricted | No Access | Limited Update | Read |
| Security Admin | Read | Read | Admin | Admin | Restricted Admin Only | Admin | Read |
| Auditor | Read | Read | Read Only | No Access | No Access | No Access | Read |

## Design Notes
- access to the jump host is restricted to approved administrative functions only,
- customer records access is not available to normal SOC analyst roles,
- model configuration is limited to authorized engineering or admin roles,
- the design separates analyst investigation functions from administrative control functions.

## Security Benefit
This reduces the attack surface, limits lateral movement opportunities, and supports stronger privilege separation.
