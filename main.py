import getpass
from customfunctions import *


def main():
    # ufw()  # Gets Firewall

    # update()  # Updating system

    change_password(input("Enter a password (Default: CyberPatriot123!@#): "))  # Changing user passwords

    remove_unauthorized_users()  # Removes unauthorized users

    create_new_users()  # Creates new users

    # secure_root()  # Secures root

    # secure_shadow()  # Secures shadow

    # remove_hacking_tools()  # Removes hacking tools

    # possible_critical_services()  # Removes or keeps possible critical services in ReadMe


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


def possible_critical_services() -> None:
    """
    Removes unneeded services that aren't listed on the ReadMe

    Installs and updates services that are needed

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
    cprint(f"\nMake sure to SECURE these services: {', '.join(exclusion)}", color="red", bold=True, underline=True)

    confirmation()



if __name__ == "__main__":
    _username = getpass.getuser()
    _password = getpass.getpass()

    main()
