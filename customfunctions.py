import os
import subprocess


def _get_command(command: str) -> list[str]:
    return command.split(" ")


def run_command(command: str) -> None:
    subprocess.run(_get_command(command), capture_output=True, text=True)


def run_commands(commands: list[str]) -> None:
    for i in range(len(commands)):
        run_command(commands[i])


def confirmation(clear=True):
    input("Press ENTER to continue...")
    if clear:
        _clear()


def _clear():
    os.system("clear")
    exit(1)


# Decoration

def print_red(string: str, bold: bool = False, underline: bool = False) -> None:
    decoration = ""
    if bold:
        decoration += "1;"
    if underline:
        decoration += "4;"
    print(f"\033[{decoration}91m{string}\033[0m")


def print_green(string: str, bold: bool = False, underline: bool = False) -> None:
    decoration = ""
    if bold:
        decoration += "1;"
    if underline:
        decoration += "4;"
    print(f"\033[{decoration}92m{string}\033[0m")


def print_yellow(string: str, bold: bool = False, underline: bool = False) -> None:
    decoration = ""
    if bold:
        decoration += "1;"
    if underline:
        decoration += "4;"
    print(f"\033[{decoration}93m{string}\033[0m")


def print_blue(string: str, bold: bool = False, underline: bool = False) -> None:
    decoration = ""
    if bold:
        decoration += "1;"
    if underline:
        decoration += "4;"
    print(f"\033[{decoration}924m{string}\033[0m")
