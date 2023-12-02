import os

def check_ssh_config():
    ssh_config_file = '/etc/ssh/sshd_config'
    if not os.path.exists(ssh_config_file):
        return "SSH configuration file not found."

    findings = []
    with open(ssh_config_file, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue  # Skip comments and empty lines

            if 'PermitRootLogin' in line and 'yes' in line.split():
                findings.append("Root login is permitted. It's recommended to disable root login.")
            
            if 'Protocol' in line and not '2' in line.split():
                findings.append("SSH Protocol version 1 is allowed. It's recommended to use only version 2.")

            # Add more checks as needed

    return findings or "No potential misconfigurations found."

def main():
    print("SSH Configuration Analysis\n---------------------------")
    ssh_config_findings = check_ssh_config()
    if isinstance(ssh_config_findings, list):
        for finding in ssh_config_findings:
            print(f"[ALERT] {finding}")
    else:
        print(ssh_config_findings)

if __name__ == "__main__":
    main()

