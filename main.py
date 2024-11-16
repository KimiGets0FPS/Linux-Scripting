import getpass
import os
import subprocess
from customfunctions import *


_username = getpass.getuser()
_password = getpass.getpass()

def main() -> None:
    run_command("sudo su")
    ufw()
    update()
    remove_unauthorized_users()
    create_new_users()


def ufw() -> None:
    """
    Installs ufw if it isn't already installed
    Enables ufw and checks if it is running
    """
    run_commands(["apt-get install ufw", "ufw enable", "ufw status"])
    print("ufw installed and enabled")

def update() -> None:
    """
    Running update and upgrade to update the system
    Getting unattended-upgrades to enable automatic updates
    """
    run_commands(["apt update -y", "apt upgrade -y"])
    print_green("System updated")
    run_commands(["apt-get install unattended-upgrades -y", "systemctl start unattended-upgrades"])
    print_green("Auto updates started")


def remove_unauthorized_users() -> None:
    ...

def create_new_users():
    ...

if __name__ == "__main__":
    main()
