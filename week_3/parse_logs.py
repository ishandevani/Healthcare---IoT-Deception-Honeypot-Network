import json

LOG_FILE = "/home/cowrie/cowrie/var/log/cowrie/cowrie.json"


def read_logs():
    logs = []

    with open(LOG_FILE, "r") as f:
        for line in f:
            try:
                logs.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    return logs


if __name__ == "__main__":
    logs = read_logs()
    print(f"Loaded {len(logs)} events.")