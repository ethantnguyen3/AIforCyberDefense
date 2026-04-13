Admin User (AST-06):
- Domain Admins ✓
- Schema Admins ✓
- Enterprise Admins ✓
- Database Admins ✓
Result: EXCESSIVE - Too many roles = Single point of failure

Service Account (svc_backup):
- Full database access ✓
- Password: NEVER EXPIRES ✓
- No MFA required ✓
Result: CRITICAL RISK - Permanent access if compromised

Jump Host Access:
- Admin accounts: Unrestricted ✓
- Standard users: SSH ALLOWED ✗ (Should be admin-only)
- Authentication: Password only (no MFA) ✗
Result: VULNERABILITY - Standard users can access privileged systems
