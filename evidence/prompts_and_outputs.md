PROMPT: Analyze these SIEM logs for attack patterns
Output: 
"No coordinated attack detected. Alerts are isolated events."
Assessment: MISSED PHISHING→MALWARE→PERSISTENCE CHAIN
This is why AI anomaly detection is needed: Current system cannot correlate
multi-stage attacks happening within 20 minutes.

PROMPT: Score these activities as normal vs. anomalous
- Login at 3:00 AM from China
- 5,000 database queries in 30 minutes
- 50 GB backup downloaded to personal laptop

Output:
AI Model Response: "Activity 1 & 2 are anomalous (95%+ confidence),
Activity 3 requires manual review."
Assessment: USEFUL - AI can reduce alert fatigue by prioritizing real threats
