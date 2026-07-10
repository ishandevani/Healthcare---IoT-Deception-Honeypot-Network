import time

from parse_logs import read_logs
from ioc_extractor import extract_iocs, print_iocs
from threat_report import generate_threat_report

while True:
    logs = read_logs()

    if logs:
        sessions = extract_iocs(logs)
        print_iocs(sessions)
        generate_threat_report(sessions)
        print(f"Processed {len(logs)} new log entries.")
    else:
        print("No new log entries found.")

    print("Waiting 30 seconds...\n")
    time.sleep(30)