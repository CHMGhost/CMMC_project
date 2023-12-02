# Security Scripts Collection

This collection of Python scripts provides various security checks for Linux systems. Each script serves a specific purpose, from scanning open ports to checking for default credentials and analyzing system configurations for potential security risks.
Scripts Overview

1. **Open Ports Check: Scans for open network ports that could be entry points for unauthorized access.
2. **Default Credentials Check: Tests services like SSH, MySQL, and PostgreSQL for default or well-known credentials.
3. **Firewall Status Check: Checks the status of common firewalls like ufw and iptables.
4. **ClamAV Antivirus Check: Verifies the installation and status of ClamAV antivirus software.
5. **User Account Review: Examines user accounts for weak password policies and unnecessary administrative privileges.
6. **SSH Configuration Analysis: Analyzes the SSH configuration for potential misconfigurations.
7. **Log Analysis: Performs basic analysis of system logs for signs of suspicious activities.
8. **Security Patches Check: Checks for the installation of critical security patches.
9. **Package Analysis: Check for out of date packages.
10. *8 Service Analysis Check for unneeded services.

## Prerequisites

- Python 3.x
- Access to a Linux-based system
- Necessary privileges to run security checks (some scripts might require superuser access)
- PostgreSQL Development Files. Install these by:
```bash
sudo apt-get install libpq-dev
```
- Python libraries as needed (e.g., paramiko, psycopg2, mysql-connector-python, nmap). Install these using pip:

```bash
pip install paramiko psycopg2 mysql-connector-python python-nmap
```
You can also use the requirements.txt to install the python libraries
```bash
pip install -r requirements.txt
```

## Installation

- Clone this repository or download the scripts to your local machine.
- Ensure all prerequisites are met.

## Usage

Each script can be run individually. Navigate to the script's directory and execute the script using Python. For example:
```bash
sudo python3 scan_ports.py
```

Replace can_ports.py with the name of the script you wish to run.

## Important Notes

- Always ensure you have the necessary permissions to run these scripts on the target system.
- Running network scans, password checks, and configuration analyses can be seen as intrusive actions. Use these scripts responsibly and ethically.
- These scripts are intended for educational and security auditing purposes. They should not be used for unauthorized testing.

## Contributing

- Contributions to this collection are welcome. Please adhere to standard coding practices and provide documentation for any additions or changes.
