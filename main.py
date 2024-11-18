import getpass
from customfunctions import *
from configServices import *

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

def search_prohibited_files() -> None:
    """
    Searches for prohibited files and logs them before deletion
    """
    cprint("Searching for prohibited files...", color="yellow")
    
    # Log media files
    run_commands([
        "echo '###MEDIA FILES###' >> pFiles.log",
        "find / -name '*.mov' -type f >> pFiles.log",
        "find / -name '*.mp4' -type f >> pFiles.log", 
        "find / -name '*.mp3' -type f >> pFiles.log",
        "find / -name '*.wav' -type f >> pFiles.log"
    ])

    # Log pictures
    run_commands([
        "echo '###PICTURES###' >> pFiles.log",
        "find / -name '*.jpg' -type f >> pFiles.log",
        "find / -name '*.jpeg' -type f >> pFiles.log"
    ])

    # Log other files
    run_commands([
        "echo '###OTHER###' >> pFiles.log",
        "find / -name '*.tar.gz' -type f >> pFiles.log",
        "find / -name '*.php' -type f >> pFiles.log", 
        "find / -name '*backdoor*.*' -type f >> pFiles.log",
        "find / -name '*backdoor*.php' -type f >> pFiles.log"
    ])

    # Log files without groups and games
    run_commands([
        "echo '###FILES WITHOUT GROUPS###' >> pFiles.log",
        "find / -nogroup >> pFiles.log",
        "echo '###GAMES###' >> pFiles.log",
        "dpkg -l | grep -i game >> pFiles.log"
    ])

    # Delete prohibited files
    cprint("Deleting prohibited files...", color="yellow")
    run_commands([
        # Audio files
        "find / -name '*.mp3' -type f -delete",
        # Video files  
        "find / -name '*.mov' -type f -delete",
        "find / -name '*.mp4' -type f -delete",
        # Picture files
        "find / -name '*.jpg' -type f -delete",
        "find / -name '*.jpeg' -type f -delete"
    ])

    # Display log
    run_command("cat pFiles.log", capture_output=False)
    
    cprint("Prohibited files have been logged and deleted", color="green")
    confirmation()
def backup_files() -> None:
    """
    Backs up files
    """
    backup_files = [
        "/etc/passwd",
        "/etc/shadow",
        "/etc/group",
        "/etc/gshadow",
        "/etc/sysctl.conf",
        "/etc/ssh/sshd_config",
        "/etc/login.defs",
        "/etc/pam.d/common-password",
        "/etc/mysql/mysql.conf.d/mysqld.cnf",
        "/etc/apache2/conf-available/security.conf"
    ]
    
    # Create a single tar.gz archive containing all backup files
    # Check if backup files exist before attempting backup
    for file_path in backup_files:
        if not os.path.exists(file_path):
            cprint(f"Warning: {file_path} does not exist", color="yellow")
            backup_files.remove(file_path)
            confirmation(clear=False)
    backup_command = "tar -czvf backup.tar.gz " + " ".join(backup_files)
    run_commands([
        backup_command,
        "ls -l backup.tar.gz"
    ])

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
"""Todo: 
    - password policy
        - needs testing
- search_prohibited_files()
    - partially done needs testing/make an exception for cypats directory
- backup_files()
    - needs testing
"""