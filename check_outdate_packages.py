import subprocess

def check_outdated_packages():
    outdated = []
    try:
        result = subprocess.run(['apt-get', '-s', 'upgrade'], stdout=subprocess.PIPE, text=True)
        for line in result.stdout.split('\n'):
            if 'upgraded,' in line:
                outdated = line.split()[0]
                break
    except Exception as e:
        print(f"Error: {e}")
    return outdated

print(f"Number of outdated packages: {check_outdated_packages()}")
