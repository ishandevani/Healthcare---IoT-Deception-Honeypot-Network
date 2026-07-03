# Filesystem Customization

## Overview

To make the Cowrie honeypot resemble a healthcare IoT patient monitoring device, several custom files and directories were added to the simulated filesystem (`honeyfs`). These files provide realistic system information, network settings, login banners, monitoring logs, and simulated patient records.

> **Note:** The contents of these files are intentionally fictional and are used only for research and honeypot simulation purposes.

---

## Files Added

| File | Purpose |
|------|---------|
| `/etc/device.conf` | Stores simulated device configuration information such as model, firmware version, serial number, and device details. |
| `/etc/network.conf` | Contains simulated network configuration including IP address, gateway, DNS, and hostname. |
| `/etc/hostname` | Defines the hostname presented by the simulated healthcare device. |
| `/etc/issue.net` | Displays a custom SSH login banner to mimic a real medical device before authentication. |
| `/opt/monitor/patients.db` | Simulated patient database used to make the honeypot appear like a patient monitoring system. |
| `/var/log/patient_data.log` | Simulated monitoring log containing fictional device events and patient monitoring activities. |

---

## Directory Structure

```text
honeyfs/
├── etc/
│   ├── device.conf
│   ├── network.conf
│   ├── hostname
│   └── issue.net
├── opt/
│   └── monitor/
│       └── patients.db
└── var/
    └── log/
        └── patient_data.log
```

---

## Example of data

1. /etc/device.conf
```
DEVICE_NAME=CMS7000
DEVICE_TYPE=Bedside Patient Monitor
MODEL=CMS7000-A
VENDOR=VitalCare Medical
FIRMWARE=2.3.4
KERNEL=Linux 4.19.152
BOOTLOADER=U-Boot 2021.01
HARDWARE_REV=Rev-2.1
SOFTWARE_BUILD=20260412
SERIAL=CMS7000-001247
DEVICE_ID=VCM-CMS7000-1247
MANUFACTURE_DATE=2025-08-11
LAST_SERVICE=2026-04-28
LOCATION=ICU Ward 2
STATUS=Operational
UPTIME=193 Days
POWER_SOURCE=AC
BATTERY_STATUS=100%
SELF_TEST=PASS
```

2. /etc/network.conf
```
HOSTNAME=ICU-MONITOR-01
DOMAIN=hospital.local
IP=192.168.10.25
MASK=255.255.255.0
GATEWAY=192.168.10.1
DNS1=192.168.10.2
DNS2=192.168.10.3
MAC=00:1E:8C:5D:72:B1
INTERFACE=eth0
LINK_SPEED=100Mbps
DHCP=Disabled
VLAN=110
NTP=192.168.10.10
SSH=Enabled
HTTPS=Enabled
TELNET=Disabled
```

3. /etc/hostname
```
ICU-MONITOR-01
```

4. /opt/monitor/patients.db
```
PatientID: DEM0001
Room: ICU-01
Status: Stable

PatientID: DEM0002
Room: ICU-02
Status: Observation

PatientID: DEM0003
Room: ICU-03
Status: Critical

PatientID: DEM0004
Room: ICU-04
Status: Stable

PatientID: DEM0005
Room: ICU-05
Status: Recovering
```

5. /var/log/patient_data.log
```
2026-06-30 08:00 Device Started
2026-06-30 08:05 Patient Monitoring Active
2026-06-30 08:08 ECG Connected
2026-06-30 08:10 Patient Monitoring Active
2026-06-30 08:11 Software Update Check: No Updates Available
2026-06-30 08:13 Network Connection Established
2026-06-30 08:25 Heart Rate Reading: 60 bpm
2026-06-30 08:36 Data Sync to Central Server: Failed - Retrying
2026-06-30 08:42 Network Connection Lost
2026-06-30 08:51 System Time Synced with NTP Server
2026-06-30 08:54 Device Self-Test: Warning - Sensor Drift Detected
2026-06-30 09:05 Battery Level: 87%
2026-06-30 09:08 Battery Low Warning
2026-06-30 09:20 SpO2 Sensor Reconnected
2026-06-30 09:32 Device Calibration Started
2026-06-30 09:36 Device Started
2026-06-30 09:48 Software Update Check: Update Available v3.6.6
2026-06-30 09:49 Remote Diagnostics Session Ended
2026-06-30 09:57 Alarm Cleared
2026-06-30 09:58 Nurse Login: nurse_rao
2026-06-30 09:59 Software Update Installed: v1.2.1
2026-06-30 10:10 Alarm Cleared
2026-06-30 10:16 Alarm Cleared
```

## Purpose

The objective of these filesystem modifications is to:

- Simulate a realistic healthcare IoT patient monitor.
- Increase the authenticity of the Cowrie honeypot.
- Encourage attackers to interact with the fake filesystem.
- Generate more realistic attack logs for cybersecurity research.
- Avoid exposing any real hospital or patient information by using only fictional data.

---

## File Contents

The sample contents for each file are provided in the following section of this repository.