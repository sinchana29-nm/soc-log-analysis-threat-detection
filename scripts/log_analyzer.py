from pathlib import Path
from collections import Counter
import re

# Find the project root relative to this script
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_ROOT / "logs" / "auth.log"

# Number of failed attempts considered suspicious
THRESHOLD = 5

failed_attempts = Counter()

with LOG_FILE.open("r", encoding="utf-8") as file:
    for line in file:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

            if match:
                ip_address = match.group(1)
                failed_attempts[ip_address] += 1


print("=== SOC Log Analysis & Threat Detection ===")
print()

if not failed_attempts:
    print("No failed login attempts detected.")
else:
    for ip_address, count in failed_attempts.items():
        print(f"IP Address: {ip_address}")
        print(f"Failed Attempts: {count}")

        if count >= THRESHOLD:
            print("ALERT: Possible brute-force attack detected!")
        else:
            print("Status: Below detection threshold")

        print("-" * 45)
