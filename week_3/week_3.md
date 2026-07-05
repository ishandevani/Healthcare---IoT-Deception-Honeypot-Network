# Week 3: Log Parsing and Threat Intelligence Extraction

## Objective

The goal of Week 3 is to analyze Cowrie honeypot logs and extract Indicators of Compromise (IoCs) using Python. The extracted threat intelligence is organized into reports for further security analysis.

---

## Tasks Completed

- Developed Python scripts to parse Cowrie JSON logs.
- Extracted Indicators of Compromise (IoCs) from captured attack data.
- Identified attacker IP addresses from SSH sessions.
- Extracted executed terminal commands from attacker activity.
- Parsed URLs and domains used in download or execution commands.
- Extracted SHA-256 malware hashes when present in logs.
- Generated a human-readable IoC report (`ioc_report.txt`).
- Generated a structured Threat Intelligence report (`threat_intelligence.xlsx`).

---

## Extracted Indicators of Compromise

The parser extracts the following IoCs:

- Attacker IP Addresses
- Malicious Domains
- Download URLs
- SHA-256 Malware Hashes
- Executed Terminal Commands

---

## Output Files

```
week_3/
│
├── main.py
├── parse_logs.py
├── ioc_extractor.py
├── threat_report.py
│
└── output/
    ├── ioc_report.txt
    └── threat_intelligence.xlsx
```

---

## Threat Intelligence Workbook

The generated Excel workbook contains four worksheets:

| Worksheet | Description |
|-----------|-------------|
| IP | Unique attacker IP addresses |
| Domain | Extracted domains from attacker commands |
| Hashes | Extracted SHA-256 malware hashes |
| URL | Extracted download URLs |

---

## Outcome

Successfully developed a Python-based log parser that automatically processes Cowrie honeypot logs, extracts key Indicators of Compromise (IoCs), and generates structured threat intelligence reports in both text and Excel formats.