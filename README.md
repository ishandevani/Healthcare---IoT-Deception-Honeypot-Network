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

what we do:

* Install Docker on Ubuntu
* Deploy Cowrie (honeypot software)
* Configure it to look like a medical IoT device

## Installation

1. Install Docker
```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
```

2. Pull Cowrie Image
```bash
sudo docker pull cowrie/cowrie
```

3. Run Cowrie Container
```bash
sudo docker run -d \
--name cowrie \
-p 2222:2222 \
-p 2223:2223 \
cowrie/cowrie
```

4. Verify Container Status
```bash
sudo docker ps
```