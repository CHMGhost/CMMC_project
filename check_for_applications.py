import subprocess

# Function to execute shell commands
def execute_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return None

# Function to check if a service is running
def check_service_running(service_name):
    status = execute_command(["systemctl", "is-active", service_name])
    return status == "active"

# Function to get the version of a service
def get_service_version(service_name, version_command):
    return execute_command(version_command)

def main():
    # Define services and their version commands
    services = {
        "apache2": ["apache2", "-v"],
        "nginx": ["nginx", "-v"],
        "mysql": ["mysql", "--version"],
        "postgresql": ["psql", "--version"]
    }

    # Check for each service
    for service, version_command in services.items():
        print(f"Checking {service}:")
        if check_service_running(service):
            print(f"  - {service} is running.")
            version = get_service_version(service, version_command)
            if version:
                print(f"  - Version: {version}")
            else:
                print(f"  - Unable to determine {service} version.")
        else:
            print(f"  - {service} is not running.")

if __name__ == "__main__":
    main()

