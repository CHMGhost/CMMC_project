import subprocess
import distro

def execute_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()

def check_security_updates_apt():
    update_command = ["apt-get", "update"]
    upgrade_command = ["apt-get", "upgrade", "-s"]
    execute_command(update_command)
    upgrade_output = execute_command(upgrade_command)
    security_updates = [line for line in upgrade_output.split('\n') if 'Inst' in line and 'security' in line]
    return security_updates

def check_security_updates_yum():
    update_command = ["yum", "check-update", "--security"]
    updates_output = execute_command(update_command)
    security_updates = [line for line in updates_output.split('\n') if line and 'Security:' in line]
    return security_updates

def main():
    distro_name = distro.id().lower()
    print(f"Checking for security updates on {distro_name}...\n")

    if "ubuntu" in distro_name or "debian" in distro_name:
        updates = check_security_updates_apt()
    elif "centos" in distro_name or "redhat" in distro_name or "fedora" in distro_name:
        updates = check_security_updates_yum()
    else:
        print(f"Unsupported Linux distribution: {distro_name}")
        return

    if updates:
        print("Pending security updates:")
        for update in updates:
            print(update)
    else:
        print("No pending security updates found.")

if __name__ == "__main__":
    main()
