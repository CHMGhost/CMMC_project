import paramiko
import mysql.connector
import psycopg2

# Function to test SSH default credentials
def test_ssh_default_creds(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=username, password=password, timeout=3)
        return True
    except Exception as e:
        print(f"SSH Error with {username}: {e}")
        return False
    finally:
        client.close()

# Function to test MySQL default credentials
def test_mysql_default_creds(ip, username, password):
    try:
        conn = mysql.connector.connect(host=ip, user=username, passwd=password)
        conn.close()
        return True
    except Exception as e:
        print(f"MySQL Error with {username}: {e}")
        return False

# Function to test PostgreSQL default credentials
def test_postgres_default_creds(ip, username, password):
    try:
        conn = psycopg2.connect(host=ip, user=username, password=password, dbname='postgres')
        conn.close()
        return True
    except Exception as e:
        print(f"PostgreSQL Error with {username}: {e}")
        return False

def main():
    default_creds = {
        'ssh': [('root', 'root'), ('admin', 'admin'), ('user', 'user'), ('test', 'test')],
        'mysql': [('root', ''), ('root', 'root'), ('admin', 'admin'), ('user', 'password')],
        'postgresql': [('postgres', ''), ('postgres', 'postgres'), ('admin', 'admin'), ('user', 'password')]
    }

    target_ip = input("Enter the target IP address: ")

    for service, creds in default_creds.items():
        for username, password in creds:
            if service == 'ssh' and test_ssh_default_creds(target_ip, username, password):
                print(f"[ALERT] Default SSH credential found: {username}@{target_ip} with password '{password}'")
            elif service == 'mysql' and test_mysql_default_creds(target_ip, username, password):
                print(f"[ALERT] Default MySQL credential found: {username}@{target_ip} with password '{password}'")
            elif service == 'postgresql' and test_postgres_default_creds(target_ip, username, password):
                print(f"[ALERT] Default PostgreSQL credential found: {username}@{target_ip} with password '{password}'")

if __name__ == "__main__":
    main()
