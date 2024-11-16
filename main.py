import getpass
import os
from customfunctions import *


def main():

    ufw()  # Gets Firewall

    update()  # Updating system

    change_password(input("Enter a password (Default: CyberPatriot123!@#): "))  # Changing user passwords

    remove_unauthorized_users()  # Removes unauthorized users

    create_new_users()  # Creates new users


def ufw() -> None:
    """
    Installs ufw if it isn't already installed

    Enables ufw and checks if it is running

    :return: None
    """
    run_commands(["apt-get install ufw", "ufw enable", "ufw status"])
    print("ufw installed and enabled")

    confirmation()

def update() -> None:
    """
    Running update and upgrade to update the system

    Getting unattended-upgrades to enable automatic updates

    :return: None
    """
    print_yellow("Updating system...")
    run_commands(["apt update -y", "apt upgrade -y"])
    print_green("System updated")

    confirmation(False)

    print_yellow("Installing unattended-upgrades...")
    run_commands(["apt-get install unattended-upgrades -y", "systemctl start unattended-upgrades"])
    print_green("Auto updates started")

    confirmation()

def change_password(password: str="CyberPatriot123!@#") -> None:
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
        print_red("ADD USERS TO normal_users.txt AND admins.txt BEFORE DOING THIS COMMAND", bold=True)
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
    print_yellow("Secure Root...")
    run_command("sudo passwd -l root")
    print_green("Root Secured")

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

    confirmation()


if __name__ == "__main__":
    _username = getpass.getuser()
    _password = getpass.getpass()

    main()