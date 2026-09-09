import re
from collections import Counter

LOG_FILE = "../logs/auth.log"
THRESHOLD = 5

failed_attempts = Counter()

with open(LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

            if match:
                ip_address = match.group(1)
                failed_attempts[ip_address] += 1

print("=== SOC Log Analysis ===")
print()

for ip, count in failed_attempts.items():
    print(f"IP Address: {ip}")
    print(f"Failed Attempts: {count}")

    if count >= THRESHOLD:
        print(" ALERT: Possible brute-force attack detected!")
    else:
        print("Status: Normal / Low activity")

    print("-" * 40)
