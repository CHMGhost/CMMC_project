import re
import collections

def analyze_auth_log(log_file_path):
    with open(log_file_path, 'r') as file:
        log_content = file.readlines()

    failed_logins = collections.defaultdict(int)
    sudo_commands = []

    for line in log_content:
        # Check for failed login attempts
        if 'Failed password' in line:
            user = re.search(r'for (\S+) from', line)
            if user:
                failed_logins[user.group(1)] += 1

        # Check for executed sudo commands
        if 'COMMAND=' in line:
            command = re.search(r'COMMAND=(.*)', line)
            if command:
                sudo_commands.append(command.group(1))

    return failed_logins, sudo_commands

def main():
    log_file_path = '/var/log/auth.log'  # Path to authentication log

    print("Analyzing System Logs for Suspicious Activities\n------------------------------------------------")
    failed_logins, sudo_commands = analyze_auth_log(log_file_path)

    print("Failed Login Attempts:")
    for user, count in failed_logins.items():
        print(f"  User: {user}, Attempts: {count}")

    if sudo_commands:
        print("\nSudo Commands Executed:")
        for command in sudo_commands:
            print(f"  {command}")

if __name__ == "__main__":
    main()

