# Threat Summary

## Key Threats

- **Ransomware Deployment:** Attackers encrypting the Customer Records Database (AST-01) to extort the organization.

- **Credential Harvesting / Privilege Escalation:** Attackers compromising a low-level endpoint and moving laterally to steal IT Administrator (AST-06) credentials.

- **Data Manipulation / Integrity Loss:** Exploitation of client-side vulnerabilities or API weaknesses to alter financial records in transit.

## Attack Surfaces

- **Inbound Email Gateways:** Primary vector for phishing and social engineering aimed at endpoints.

- **App & API:** The application acts as a public-facing attack surface. Current baseline testing reveals UI terminology confusion (e.g., inaccurate use of the term "profit") and critical data persistence issues (users losing records upon closing the app), which could be leveraged to cause data desynchronization or manipulated via local storage tampering (AST-09).

- **Internal Routing:** The pathways managed by the 3560 Layer 3 switch and Jump Host.

## Misuse Scenarios

- An employee falls for a phishing email, allowing a malicious payload to execute on their endpoint. The malware attempts to scan the network, bypass the Jump Host, and query the DBMS.

- An attacker reverse-engineers the mobile application to exploit the known data persistence bugs, injecting malformed sales/expense records into the Core API Gateway to corrupt the backend database.

## Likely Impact

- Severe financial and reputational damage due to PII exposure, loss of database availability (ransomware), and degradation of client trust if financial tracking data is lost or corrupted.
