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
pip install cowrie
```

4. Configure as Medical IoT Device
```bash
cp src/cowrie/data/etc/cowrie.cfg.dist etc/cowrie.cfg
nano etc/cowrie.cfg
```

Key settings changed:
* hostname = ICU-MONITOR-01
* version_string = SSH-2.0-dropbear_2020.81
* telnet enabled = true
* arch = linux-arm-lsb

5. redirect port:
```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-ports 2222
sudo iptables -t nat -A PREROUTING -p tcp --dport 23 -j REDIRECT --to-ports 2223
```

6. Start Cowrie
```bash
bin/cowrie start
bin/cowrie status
```

## Healthcare IoT Device Simulation

The honeypot was customized to resemble a hospital patient monitoring device.

### Custom Hostname

```
ICU-MONITOR-01
```

---

### Login Banner

Modified `/etc/issue.net`

```
GE Healthcare CMS7000 Patient Monitoring System

Authorized Access Only
Hospital Internal Network
All activity is monitored.
```

---

### Custom Healthcare Files

Created healthcare-specific files inside the virtual filesystem.

```
honeyfs/
├── etc
│   ├── device.conf
│   ├── hostname
│   ├── issue.net
│   └── network.conf
├── home
│   └── admin
├── opt
│   └── monitor
│       └── patients.db
└── var
    └── log
        └── patient_data.log
```

---

### Simulated Files

| File | Purpose |
|-------|----------|
| `/etc/device.conf` | Device configuration |
| `/etc/network.conf` | Network configuration |
| `/etc/hostname` | Healthcare device hostname |
| `/etc/issue.net` | Login banner |
| `/opt/monitor/patients.db` | Simulated patient database |
| `/var/log/patient_data.log` | Simulated monitoring log |

---

## SSH Configuration

Configured Cowrie to listen for SSH connections.

Example:

```ini
listen_endpoints = tcp:2222:interface=0.0.0.0
```

---

## Verification

Verified the following.

- Cowrie service started successfully.
- SSH connection established.
- Fake healthcare login banner displayed.
- Healthcare hostname configured.
- Virtual filesystem customized.
- Honeypot ready for attacker interaction.

---
