# Incident Investigation Report

## 1. Executive Summary

A simulated authentication log was analyzed to identify suspicious login activity.

The analysis detected multiple failed SSH authentication attempts originating from the same IP address, followed by a successful login. This pattern is consistent with a potential brute-force attack followed by successful authentication.

> **Note:** All activity and IP addresses in this project are simulated for educational purposes.

---

## 2. Detection Summary

| Field | Details |
|---|---|
| Detection Type | Possible Brute-Force Attack |
| Source IP | 185.220.101.14 |
| Failed Attempts | 6 |
| Successful Login | Yes |
| Detection Threshold | 5 failed attempts |
| Severity | Medium |
| Status | Detected |

---

## 3. Evidence

The following authentication events were observed from the same source IP:

09:01:12 - Failed login  
09:01:18 - Failed login  
09:01:25 - Failed login  
09:01:31 - Failed login  
09:01:39 - Failed login  
09:01:46 - Failed login  
09:02:03 - Successful login

The six failed attempts occurred within approximately one minute, followed by a successful authentication from the same IP address.

---

## 4. Investigation

The Python log analyzer extracted source IP addresses from failed authentication events and counted the number of failures associated with each IP.

The configured detection threshold was **5 failed attempts**.

The source IP **185.220.101.14** generated **6 failed attempts**.

Since the number of failures exceeded the threshold, the script generated a brute-force detection alert.

---

## 5. Other Observed Activity

Two additional source IP addresses were observed:

| Source IP | Failed Attempts | Result |
|---|---:|---|
| 10.0.0.25 | 1 | Below threshold |
| 203.0.113.45 | 3 | Below threshold |

These addresses did not reach the configured detection threshold.

---

## 6. Recommended Mitigations

For a real environment, the following controls could help reduce the risk:

- Enable multi-factor authentication (MFA)
- Implement account lockout or rate limiting
- Restrict SSH access to trusted networks where possible
- Monitor repeated authentication failures
- Review successful logins following repeated failures
- Use centralized logging and SIEM alerting
- Investigate and block confirmed malicious sources according to organizational policy

---

## 7. Conclusion

The analysis successfully identified a simulated authentication pattern consistent with a potential brute-force attack.

The Python-based detection script demonstrated how repetitive authentication failures can be automatically identified and converted into a security alert.

This project demonstrates basic SOC capabilities including:

- Log analysis
- Authentication monitoring
- Pattern recognition
- Threat detection
- Alert generation
- Incident documentation
