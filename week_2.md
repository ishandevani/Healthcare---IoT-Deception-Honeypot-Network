# Week 2: Exposure and Data Capture

## Objective

Configure Cowrie to capture attacker activities and forward honeypot logs to Splunk for centralized monitoring and analysis. This enables real-time visibility into login attempts, command execution, and attacker behavior.

---

## Project Task

- Configure Cowrie JSON logging.
- Integrate Cowrie logs with Splunk Enterprise.
- Verify that attacker activities are successfully ingested into Splunk.
- Test the logging pipeline using SSH login attempts.
- Prepare the environment for threat analysis dashboards in Week 3.

---

## Environment

| Component | Version |
|----------|---------|
| Ubuntu Server | 24.04 LTS |
| Cowrie Honeypot | Latest |
| Splunk Enterprise | Latest |
| Python | 3.x |

---

## Architecture

```
Attacker
    │
    ▼
Cowrie Honeypot
    │
    ▼
cowrie.json
    │
    ▼
Splunk Enterprise
    │
    ▼
Search & Dashboard
```

---

## Configuration Steps

### 1. Verify Cowrie JSON Logging

Confirm that Cowrie generates JSON logs.

```bash
tail -f ~/cowrie/var/log/cowrie/cowrie.json
```

---

### 2. Configure Splunk Data Input

Add the Cowrie log file to Splunk.

**Path**

```
/home/cowrie/cowrie/var/log/cowrie/cowrie.json
```

Configuration:

- Source Type: `cowrie:json`
- Index: `cowrie`

---

### 3. Restart Splunk

```bash
sudo /opt/splunk/bin/splunk restart
```

---

### 4. Generate Test Events

Connect to the Cowrie SSH service using incorrect and valid credentials.

Example:

```bash
ssh admin@<Cowrie-IP> -p 2222
```

Attempt multiple login attempts to generate logs.

---

### 5. Verify Logs in Splunk

Search all Cowrie events.

```spl
index="cowrie"
```

Failed login attempts.

```spl
index="cowrie" eventid="cowrie.login.failed"
```
![Splunk2](/Screenshots/Splunk2.png)

Successful login.

```spl
index="cowrie" eventid="cowrie.login.success"
```
![Splunk3](/Screenshots/Splunk3.png)

Commands executed.

```spl
index="cowrie" eventid="cowrie.command.input"
```
![Splunk1](/Screenshots/Splunk1.png)

---

## Results

The following attacker activities were successfully captured and indexed into Splunk:

- Failed SSH login attempts
- Successful logins
- Username and password attempts
- Executed shell commands
- Session information
- Source IP addresses
- Event timestamps

---

## Outcome

Successfully integrated Cowrie Honeypot with Splunk Enterprise. The centralized logging pipeline now collects attacker activities in real time, providing a foundation for threat analysis, visualization, and dashboard creation in the next phase of the project.

---

## Next Week

Week 3 focuses on:

- Parsing Cowrie logs using Python
- Extracting Indicators of Compromise (IoCs)
- Building custom threat intelligence datasets
- Preparing data for visualization dashboards