AI Anomaly Detection Pipeline (Detect): Implementation of machine learning models on the SIEM to baseline normal network and user behavior, correlating multi-stage events (e.g., an email click followed by an unusual PowerShell execution).

Automated SOAR Playbooks (Respond): Scripts that trigger upon high-confidence AI alerts to instantly isolate compromised endpoints (AST-06) from the network and revoke user Active Directory tokens.

Strict Default-Deny ACLs (Protect): Hardening the 3560 Layer 3 Switch configurations to strictly limit traffic types allowed across trust boundaries, heavily restricting access to the Jump Host.

Application Code Remediation (Protect): Updating the application to fix state-saving data persistence bugs 
