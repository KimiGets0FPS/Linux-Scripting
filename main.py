import getpass
from customfunctions import *


def main():
    ufw()  # Gets Firewall

    update()  # Updating system

    change_password(input("Enter a password (Default: CyberPatriot123!@#): "))  # Changing user passwords

    remove_unauthorized_users()  # Removes unauthorized users

    create_new_users()  # Creates new users

    secure_root()  # Secures root

    secure_etc_files()  # Secures etc files

    remove_hacking_tools()  # Removes hacking tools

    possible_critical_services()  # Removes or keeps possible critical services in ReadMe
    


def ufw() -> None:
    """
    Installs ufw if it isn't already installed

    Enables ufw and checks if it is running

    :return: None
    """
    run_commands(["apt-get install ufw", "ufw enable", "ufw status"])
    cprint("ufw installed and enabled", color="green")

    confirmation()


def update() -> None:
    """
    Running update and upgrade to update the system

    Getting unattended-upgrades to enable automatic updates

    :return: None
    """
    cprint("Updating system...", color="yellow")
    run_commands(["apt update -y", "apt upgrade -y"])
    cprint("System updated", color="green")

    confirmation(False)

    cprint("Installing unattended-upgrades...", color="yellow")
    run_commands(["apt-get install unattended-upgrades -y", "systemctl start unattended-upgrades"])
    cprint("Auto updates started", color="green")

    confirmation()


def media_files() -> None:
    """
    Finds all media files
    :return:
    """
    cprint("Pictures: ", color="magenta", bold=True)
    for extension in "jpeg jpg png tiff gif svg bmp webp".split(" "):
        run_command(f"locate /home *.{extension}")
    confirmation()

    cprint("Videos: ", color="magenta", bold=True)
    for extension in "mov mp4 wmv avi mkv webm flv avchd".split(" "):
        run_command(f"locate /home *.{extension}")
    confirmation()

    cprint("Audio: ", color="magenta", bold=True)
    for extension in "wav mp3 aiff aac alac m4a flac wma".split(" "):
        run_command(f"locate /home *.{extension}")
    confirmation()

    cprint("Others: ", color="magenta", bold=True)
    for extension in "tar.gz php".split(" "):
        run_command(f"locate / *.{extension}")
    confirmation()


def change_password(password: str = "CyberPatriot123!@#") -> None:
    """
    :param password: Password to change to (Default: CyberPatriot123!@#)

    :return: None
    """
    return



def remove_unauthorized_users() -> None:
    """
    Removes unauthorized users not listed in normal_users.txt

    Valid users are provided in the CyberPatriot ReadMe file

    :return: None
    """
    normal_users = open("normal_users.txt", "r").read().splitlines()
    sudoers = open("admins.txt", "r").read().splitlines()

    if not normal_users or not sudoers:
        cprint("ADD USERS TO normal_users.txt AND admins.txt BEFORE DOING THIS COMMAND", color="red", bold=True)
        confirmation()
        return

    confirmation()


def create_new_users() -> None:
    """
    Creates users from normal_users.txt
    """
    return
    # new_users = open("new_users.txt", "r").read().splitlines()
    #
    # confirmation()


def secure_root() -> None:
    """
    Secures Root

    :return: None
    """
    cprint("Secure Root...", color="yellow")
    run_command("sudo passwd -l root")
    cprint("Root Secured", color="green")

    confirmation()


def secure_etc_files() -> None:
    """
    Securing /etc/shadow
    
    :return: None
    """
    run_commands(["sudo chmod 640 /etc/shadow", "ls -l /etc/shadow",
                  "sudo chmod 644 /etc/passwd", "ls -l /etc/passwd",
                  "sudo chmod 644 /etc/group", "ls -l /etc/group",
                  "sudo chmod 644 /etc/gshadow", "ls -l /etc/gshadow"])

    confirmation()


def remove_hacking_tools() -> None:
    """
    Removes all hacking tools

    :return: None
    """
    hacking_tools = ["john", "hydra", "nginx", "wireshark", "ophcrack", "nikto", "tcpdump", "nmap", "zenmap", "deluge"]
    for i in range(len(hacking_tools)):
        cprint(f"Removing {hacking_tools[i]}", color="blue")
        run_command(f"apt-get purge {hacking_tools[i]} -y", capture_output=False)

    run_command("apt-get autoremove -y", capture_output=False)
    cprint("Hacking tools removed!", color="green")

    confirmation()


def possible_critical_services() -> None:
    """
    Removes unneeded services that aren't listed on the ReadMe

    Installs and updates services that are needed
    Secures known services
    :return: None
    """
    services = ["openssh-server", "openssh-client", "samba", "apache2", "vsftpd", "snmp", "x11vnc"]
    exclusion = input("Critical services to add to exclusion list (must be program name and seperated by comma): ").split(", ")

    for i in range(len(services)):
        if services[i] not in exclusion:
            cprint(f"Removing {services[i]}", color="yellow")
            run_command(f"apt-get purge {services[i]} -y", capture_output=False)
            cprint(f"Removed {services[i]}", color="green")
        else:
            cprint(f"Ignoring {services[i]}...", color="blue")

    cprint("Finishing up...", color="yellow")
    run_command("apt-get autoremove -y")
    cprint("Unneeded Services Removed!", color="green")

    for i in range(len(exclusion)):
        cprint(f"Installing and upgrading {exclusion[i]}", color="yellow")
        run_commands([f"apt-get install {exclusion[i]} -y", f"apt-get upgrade {exclusion[i]}"], capture_output=False)
        cprint(f"Done installing and upgrading {exclusion[i]}", color="green")

    cprint("Critical Services Installed!", color="green")
    cprint("SECURING known services...", color="yellow")
    for i in range(len(exclusion)):
        cprint(f"Securing {exclusion[i]}", color="blue")
        if exclusion[i] == "openssh-server":
            openssh_config()
        elif exclusion[i] == "mysql":
            mysql_config()
        elif exclusion[i] == "apache2":
            apache2_config()
        elif exclusion[i] == "samba":
            samba_config()
        elif exclusion[i] == "vsftpd":
            vsftpd_config()
        elif exclusion[i] == "x11vnc":
            x11vnc_config()
        elif exclusion[i] != "openssh-server" or "mysql" or "apache2" or "samba" or "vsftpd" or "x11vnc":
            cprint(f"{exclusion[i]} is not a known service make sure to secure it manually", color="red")
    cprint("Known services secured!", color="green")
    
    confirmation()
    
def config_sysctl() -> None:
    """
    Configs sysctl

    :return: None
    """
    run_commands([
        "sed -i '$a net.ipv6.conf.all.disable_ipv6 = 1' /etc/sysctl.conf",
        "sed -i '$a net.ipv6.conf.default.disable_ipv6 = 1' /etc/sysctl.conf",
        "sed -i '$a net.ipv6.conf.lo.disable_ipv6 = 1' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.conf.all.rp_filter=1' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.conf.all.accept_source_route=0' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.tcp_max_syn_backlog = 2048' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.tcp_synack_retries = 2' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.tcp_syn_retries = 5' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.tcp_syncookies=1' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.ip_foward=0' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.conf.all.send_redirects=0' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.conf.default.send_redirects=0' /etc/sysctl.conf"
    ])

    run_command("sysctl -p", capture_output=False)
    cprint("Sysctl configured", color="green")

    confirmation()

def openssh_config() -> None:
    """
    Configs ssh
    """
    run_commands([
        "sed -i 's/LoginGraceTime .*/LoginGraceTime 60/g' /etc/ssh/sshd_config",
        "sed -i 's/PermitRootLogin .*/PermitRootLogin no/g' /etc/ssh/sshd_config",
        "sed -i 's/Protocol .*/Protocol 2/g' /etc/ssh/sshd_config",
        "sed -i 's/#PermitEmptyPasswords .*/PermitEmptyPasswords no/g' /etc/ssh/sshd_config",
        "sed -i 's/PasswordAuthentication .*/PasswordAuthentication yes/g' /etc/ssh/sshd_config",
        "sed -i 's/X11Forwarding .*/X11Forwarding no/g' /etc/ssh/sshd_config"
    ])
    run_command("systemctl restart openssh-server", capture_output=False)
    cprint("Openssh configured", color="green")

    confirmation()
    
def mysql_config() -> None:
    """
    Configs mysql
    """
    run_commands([
        "sed -i 's/bind-address .*/bind-address = 127.0.0.1/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/skip-external-locking .*/skip-external-locking = 1/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/key_buffer_size .*/key_buffer_size = 32M/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/max_allowed_packet .*/max_allowed_packet = 16M/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/thread_stack .*/thread_stack = 256K/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/thread_cache_size .*/thread_cache_size = 8/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/query_cache_limit .*/query_cache_limit = 1M/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/tmp_table_size .*/tmp_table_size = 16M/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/max_heap_table_size .*/max_heap_table_size = 16M/g' /etc/mysql/mysql.conf.d/mysqld.cnf"
    ])
    run_command("systemctl restart mysql", capture_output=False)
    cprint("Mysql configured", color="green")

    confirmation()

def apache2_config() -> None:
    """
    Configs apache2
    """
    run_commands([
        "sed -i 's/ServerTokens .*/ServerTokens Prod/g' /etc/apache2/conf-available/security.conf",
        "sed -i 's/ServerSignature .*/ServerSignature Off/g' /etc/apache2/conf-available/security.conf"
    ])
    run_command("systemctl restart apache2", capture_output=False)
    cprint("Apache2 configured", color="green")

    confirmation()

def samba_config() -> None:
    """
    Configs samba
    """
    return

def vsftpd_config() -> None:
    """
    Configs vsftpd
    """
    return

def x11vnc_config() -> None:
    """
    Configs x11vnc
    """
    return

def password_policy_config() -> None:
    """
    Configs password policy
    """
    run_commands([ #/etc/login.defs
        "sed -i 's/PASS_MAX_DAYS .*/PASS_MAX_DAYS 90/g' /etc/login.defs",
        "sed -i 's/PASS_MIN_DAYS .*/PASS_MIN_DAYS 10/g' /etc/login.defs",
        "sed -i 's/PASS_WARN_AGE .*/PASS_WARN_AGE 7/g' /etc/login.defs"
    ])
    run_commands([ #/etc/pam.d/common-password
        "sed -i 's/minlen .*/minlen 14/g' /etc/pam.d/common-password",
        "sed -i 's/dcredit .*/dcredit -1/g' /etc/pam.d/common-password",
        "sed -i 's/ucredit .*/ucredit -1/g' /etc/pam.d/common-password",
        "sed -i 's/lcredit .*/lcredit -1/g' /etc/pam.d/common-password",
        "sed -i 's/ocredit .*/ocredit -1/g' /etc/pam.d/common-password"
    ])
    cprint("Password policy configured", color="green")
    confirmation()

if __name__ == "__main__":
    _username = getpass.getuser()
    _password = getpass.getpass()

    main()
"""Todo: create config functions for each service
- openssh-server done
- openssh-client done
- mysql done
- apache2 done
- samba 
    - func declared needs to be done
- vsftpd 
    - func declared needs to be done
- x11vnc 
    - func declared needs to be done
- maybe put configs for services in a different file?
- password policy done (needs testing)"""