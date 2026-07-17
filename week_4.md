# Week 4: Dashboarding and Geolocation Analysis

## Objective

The objective of Week 4 is to visualize honeypot activity using Splunk dashboards and enrich attacker information with IP geolocation. This provides a better understanding of attacker behavior and improves threat analysis.

---

## Tasks Completed

- Configured a Splunk dashboard to visualize Cowrie honeypot events.
- Created dashboard panels for monitoring attacker activity.
- Developed a Python script to perform IP geolocation lookup.
- Extracted geographic information from public attacker IP addresses.
- Generated a geolocation report in Excel format.
- Began categorizing attacker activity based on executed commands.

---

## Splunk Dashboard

The dashboard includes the following visualizations:

- Total SSH Connections
- Failed Login Attempts
- Successful Login Attempts
- Top Attacker IP Addresses
- Most Targeted Usernames
- Most Used Passwords
- Executed Commands
- Command Timeline
- Payload Download Attempts
- Active Sessions

![Dashboard](/Screenshots/Dashboard.png)

---

## IP Geolocation

A Python script reads attacker IP addresses extracted during Week 3 and performs geolocation lookups using a public IP geolocation API.

The generated report includes:

- IP Address
- Country
- Region
- City
- Latitude
- Longitude
- ISP

Private IP addresses are automatically ignored during the lookup process.

---

## Project Structure

```
week_4/
│
├── main.py
├── geolocation.py
├── dashboard.md
│
└── output/
    └── geolocation_report.xlsx
```

---

## Technologies Used

- Python
- Splunk Enterprise
- Cowrie Honeypot
- OpenPyXL
- Requests
- IP-API Geolocation Service

---

## Outcome

Successfully enhanced the honeypot project by creating a Splunk monitoring dashboard and enriching attacker IP addresses with geographic information. These improvements provide better visibility into attack sources and support more effective threat analysis.