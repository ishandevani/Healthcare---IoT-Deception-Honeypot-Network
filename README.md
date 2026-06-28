# Healthcare - IoT Deception Honeypot Network

## Description
A Healthcare IoT Deception Honeypot Network built using Cowrie, Docker, Python, and Splunk to simulate vulnerable medical IoT devices, capture attacker activities, and analyze threats through security monitoring and visualization.

# Features

* Healthcare IoT device simulation
* Cowrie honeypot deployment
* SSH/Telnet attack monitoring
* Attacker activity logging
* Malware file capture
* Docker-based isolation
* Python log analysis
* Splunk dashboard visualization
* Threat intelligence generation
* Attack source IP tracking

# Technologies Used

* Ubuntu 22.04
* Cowrie Honeypot
* Docker
* Python 3
* Splunk Enterprise
* Git & GitHub
* SSH/Telnet Protocols

# Week 1: Environment Setup and Device Simulation

What we do:

* Install Cowrie on Ubuntu
* Configure it to look like a GE Healthcare CMS7000 Patient Monitor
* Set fake SSH banner, hostname, and filesystem

## Installation

1. Install Dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3-venv python3-dev libssl-dev libffi-dev build-essential
```

2. Create Cowrie User
```bash
sudo adduser --disabled-password cowrie
sudo su - cowrie
```

3. Clone and Install Cowrie
```bash
git clone https://github.com/cowrie/cowrie
cd cowrie
python3 -m venv cowrie-env
source cowrie-env/bin/activate
pip install -r requirements.txt
```

4. Configure as Medical IoT Device
```bash
cp etc/cowrie.cfg.dist etc/cowrie.cfg
nano etc/cowrie.cfg
```

Key settings changed:
* hostname = ICU-MONITOR-04
* version_string = SSH-2.0-dropbear_2020.81
* telnet enabled = true
* arch = linux-arm-lsb

5. Start Cowrie
```bash
bin/cowrie start
bin/cowrie status
```

## Device Simulation Details

* Device Model: GE Healthcare CMS7000
* Hostname: ICU-MONITOR-04
* SSH Banner: SSH-2.0-dropbear_2020.81
* SSH Port: 2222
* Telnet Port: 2223
* Default Credentials: root/root, admin/admin

## What Gets Logged

* Attacker IP address
* Username and password attempts
* Every command typed
* Files uploaded or downloaded
* Full session recording