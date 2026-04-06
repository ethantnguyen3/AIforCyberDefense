# AIforCyberDefense 
Objective & Scope 
We need to design and propose a theoretical AI-driven Security Operations Center (SOC) framework that dramatically reduces analyst alert fatigue and identifies stealthy, multi-stage attacks across an enterprise network.
The project will demonstrate how machine learning can shift a security posture from reactive (relying on human analysts to manually spot isolated alerts) to proactive (using AI to automatically correlate complex network and endpoint behaviors to stop breaches before data is exfiltrated). 
Scope:
Architecture Design: Mapping out the conceptual enterprise network, including specific subnets, VLANs, and Access Control Lists (ACLs), to identify exactly where the AI will pull its telemetry and monitor traffic.
Data Pipeline Strategy: Outlining how raw security logs are ingested and stored. This includes proposing the database schema for the security data lake and discussing the scripting logic (such as Python data normalization) needed to translate disparate logs into a unified format for the AI.
Threat Modeling: Selecting one or two specific, multi-stage attack scenarios (e.g., a phishing email leading to lateral movement and credential theft) to illustrate exactly how the AI detects the anomaly.
Response Playbooks: Defining the automated steps the AI system takes once a threat is confirmed (Security Orchestration, Automation, and Response).
