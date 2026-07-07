from collections import defaultdict


def extract_iocs(logs):
    sessions = defaultdict(dict)

    for log in logs:

        session = log.get("session")

        if not session:
            continue

        sessions[session]["src_ip"] = log.get("src_ip", "Unknown")
        sessions[session]["timestamp"] = log.get("timestamp", "Unknown")

        event = log.get("eventid")

        # Successful login
        if event == "cowrie.login.success":
            sessions[session]["username"] = log.get("username")
            sessions[session]["password"] = log.get("password")
            sessions[session]["status"] = "Success"

        # Failed login
        elif event == "cowrie.login.failed":
            sessions[session]["username"] = log.get("username")
            sessions[session]["password"] = log.get("password")
            sessions[session]["status"] = "Failed"

        # Commands
        elif event == "cowrie.command.input":
            sessions[session].setdefault("commands", []).append(
                log.get("input")
            )

    return sessions


def print_iocs(sessions):

    report = []

    report.append("========== Indicators of Compromise ==========\n")

    for session, data in sessions.items():

        report.append(f"Session ID : {session}")
        report.append(f"Attacker IP: {data.get('src_ip','-')}")
        report.append(f"Username   : {data.get('username','-')}")
        report.append(f"Password   : {data.get('password','-')}")
        report.append(f"Status     : {data.get('status','-')}")

        commands = data.get("commands", [])

        if commands:
            report.append("Commands")
            for cmd in commands:
                report.append(f"   - {cmd}")

        report.append(f"Time       : {data.get('timestamp','-')}")
        report.append("-" * 60)

    output = "\n".join(report)

    print(output)

    with open("output/ioc_report.txt", "w") as f:
        f.write(output)

    print("\nIoC report saved to output/ioc_report.txt")