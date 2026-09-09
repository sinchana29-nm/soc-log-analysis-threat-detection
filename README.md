# SOC Log Analysis & Threat Detection

##  Project Overview

This project demonstrates a practical Security Operations Center (SOC) workflow for analyzing authentication logs, identifying suspicious login activity, and investigating potential brute-force attacks.

The project uses simulated security logs and Python-based analysis to detect repeated failed login attempts and other suspicious authentication patterns.

---

##  Objectives

- Analyze authentication logs for suspicious activity
- Detect repeated failed login attempts
- Identify potential brute-force attacks
- Investigate suspicious source IP addresses
- Generate security alerts using Python
- Document findings and recommended mitigations

---

##  Tools & Technologies

- Python
- Linux
- Log Analysis
- Authentication Logs
- Cybersecurity Investigation
- Git & GitHub

---

##  Detection Scenarios

The project focuses on identifying:

- Multiple failed login attempts from the same IP
- Repeated authentication failures within a short period
- Successful login following multiple failed attempts
- Suspicious authentication patterns

---

##  Project Structure

```text
soc-log-analysis-threat-detection/
│
├── logs/
│   └── auth.log
│
├── scripts/
│   └── log_analyzer.py
│
├── reports/
│   └── incident_report.md
│
└── README.md
