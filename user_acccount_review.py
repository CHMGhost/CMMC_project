import subprocess
import pwd
import spwd
import grp

def execute_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()

def get_all_users():
    return [user.pw_name for user in pwd.getpwall() if user.pw_uid >= 1000 and 'nologin' not in user.pw_shell]

def check_user_sudo(user):
    try:
        groups = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]
        gid = pwd.getpwnam(user).pw_gid
        groups.append(grp.getgrgid(gid).gr_name)
        return 'sudo' in groups or 'admin' in groups
    except KeyError:
        return False

def get_password_policy(user):
    try:
        policy = spwd.getspnam(user)
        return {
            "Last password change": policy.sp_lstchg,
            "Password expires": policy.sp_expire,
            "Password inactive": policy.sp_inact,
            "Account expires": policy.sp_expire
        }
    except PermissionError:
        return "Permission denied. Cannot access password policy."
    except KeyError:
        return "No password policy information available."

def main():
    users = get_all_users()
    print("User Account Review\n-------------------")
    for user in users:
        print(f"User: {user}")
        print(f"  Has sudo privileges: {'Yes' if check_user_sudo(user) else 'No'}")
        print(f"  Password Policy: {get_password_policy(user)}\n")

if __name__ == "__main__":
    main()

