import getpass
import os
import subprocess
from customfunctions import *


_username = getpass.getuser()
_password = getpass.getpass()

def main() -> None:
    run_command("sudo su")
    ufw()


def ufw() -> None:
    run_commands(["apt-get install ufw", "ufw enable", "ufw status"])

def update() -> None:
    run_commands(["apt update -y", "apt upgrade -y"]) # Updates
    run_commands(["apt-get install unattended-upgrades -y"]) # Auto-Updates

def remove_unauthorized_users() -> None:
    ...


if __name__ == "__main__":
    main()
