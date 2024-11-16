import getpass
import os
from customfunctions import *


def main():
    ufw()  # Gets Firewall

    update()  # Updating system

    # change_password(input("Enter a password (Default: CyberPatriot123!@#): "))  # Changing user passwords

    # remove_unauthorized_users()  # Removes unauthorized users

    # create_new_users()  # Creates new users

    # secure_root()  # Secures root

    # secure_shadow()  # Secures shadow

    # remove_hacking_tools()  # Removes hacking tools

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


def change_password(password: str = "CyberPatriot123!@#") -> None:
    """
    :param password: Password to change to (Default: CyberPatriot123!@#)

    :return: None
    """


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
    new_users = open("new_users.txt", "r").read().splitlines()

    confirmation()


def secure_root() -> None:
    """
    Secures Root

    :return: None
    """
    cprint("Secure Root...", color="yellow")
    run_command("sudo passwd -l root")
    cprint("Root Secured", color="green")

    confirmation()


def secure_shadow() -> None:
    """
    Securing /etc/shadow

    :return: None
    """
    run_commands(["sudo chmod 640 /etc/shadow", "ls -l /etc/shadow"])

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


def possible_critical_services():
    services = ["openssh-server", "openssh-client", "samba", "apache2", "vsftpd", "ftp", "snmp"]
    for i in range(len(services)):
        if run_command(f"dpkg -l | grep -i {services[i]}", shell=True, capture_output=True, text=True) == 0:
            remove = input(f"Would you like to remove {services[i]} (y/n):").lower()[0] == "y"
            if remove:
                cprint("REMOVE", color="red")
            else:
                cprint("KEEP", color="green")




if __name__ == "__main__":
    _username = getpass.getuser()
    _password = getpass.getpass()

    main()
