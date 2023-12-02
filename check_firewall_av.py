import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()

def check_firewall_status():
    firewalls = {
        "ufw": ["ufw", "status"],
        "iptables": ["iptables", "-L"]
    }
    
    print("Firewall Status Check\n---------------------")
    for fw, cmd in firewalls.items():
        status, output = execute_command(cmd)
        if status:
            print(f"{fw.upper()} is active:\n{output}\n")
        else:
            print(f"{fw.upper()} is inactive or not installed.\nError: {output}\n")

def check_clamav_status():
    print("ClamAV Status Check\n-------------------")
    try:
        clamav_status, clamav_output = execute_command(["clamscan", "--version"])
        if clamav_status:
            print(f"ClamAV is installed:\n{clamav_output}\n")
    except FileNotFoundError:
        print("ClamAV is not installed or not found in the PATH.\n")

def main():
    check_firewall_status()
    check_clamav_status()

if __name__ == "__main__":
    main()