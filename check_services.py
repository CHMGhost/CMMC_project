import subprocess

# Function to execute shell commands
def execute_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

# Function to check if a service is running
def is_service_running(service_name):
    status = execute_command(["systemctl", "is-active", service_name])
    return status == "active"

def main():
    # List of services that shouldn't be running
    unwanted_services = ["ssh", "vsftpd", "cron"]

    for service in unwanted_services:
        if is_service_running(service):
            print(f"[WARNING] Unwanted service '{service}' is currently running.")
        else:
            print(f"[OK] Service '{service}' is not running.")

if __name__ == "__main__":
    main()

