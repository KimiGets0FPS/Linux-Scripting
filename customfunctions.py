import os
import subprocess

def _get_command(command: str) -> list[str]:
    return command.split(" ")


def run_command(command: str, stdin: bool=None, input: bool=None, stdout: bool=None, stderr: bool=None, capture_output: bool=True, shell: bool=False, cwd: bool=None, timeout: bool=None, check: bool=False, encoding: bool=None, errors: bool=None, text: bool=None, env:bool=None, universal_newlines:bool=None) -> None:
    """
    Runs a single linux command using the subprocess module

    Used by the run_commands function to run multiple commands

    Easier to use compared to the original subprocess.run() function

    :param command:
    :param stdin:
    :param input:
    :param stdout:
    :param stderr:
    :param capture_output:
    :param shell:
    :param cwd:
    :param timeout:
    :param check:
    :param encoding:
    :param errors:
    :param text:
    :param env:
    :param universal_newlines:
    :return: None
    """
    subprocess.run(_get_command(command), stdin=stdin, input=input, stdout=stdout, stderr=stderr, capture_output=capture_output, shell=shell, cwd=cwd, timeout=timeout, check=check, encoding=encoding, errors=errors, text=text, env=env, universal_newlines=universal_newlines)


def run_commands(commands: list[str], stdin: bool=None, input: bool=None, stdout: bool=None, stderr: bool=None, capture_output: bool=True, shell: bool=False, cwd: bool=None, timeout: bool=None, check: bool=False, encoding: bool=None, errors: bool=None, text: bool=None, env: bool=None, universal_newlines: bool=None) -> None:
    """
    Runs multiple linux commands using the subprocess module

    Uses the run_command function to reduce the number of times called

    :param commands:
    :param stdin:
    :param input:
    :param stdout:
    :param stderr:
    :param capture_output:
    :param shell:
    :param cwd:
    :param timeout:
    :param check:
    :param encoding:
    :param errors:
    :param text:
    :param env:
    :param universal_newlines:
    :return: None
    """
    for i in range(len(commands)):
        run_command(commands[i], stdin=stdin, input=input, stdout=stdout, stderr=stderr, capture_output=capture_output, shell=shell, cwd=cwd, timeout=timeout, check=check, encoding=encoding, errors=errors, text=text, env=env, universal_newlines=universal_newlines)


def confirmation(clear=True) -> None:
    input("Press ENTER to continue...")
    if clear:
        _clear()


def _clear() -> None:
    os.system("clear")


# Decoration

def cprint(text: str, color: str="default", end: str="\n", bold: bool=False, underline: bool=False) -> None:
    colors = {"default": "89m", "grey": "90m", "red": "91m", "green": "92m", "yellow": "93m", "blue": "94m", "magenta": "95m", "cyan": "96m", "white": "97m"}

    print(f"\033[{_get_decoration(bold=bold, underline=underline)}{colors.get(color.lower())}{text}\033[0m", end=end)


def _get_decoration(bold: bool=False, underline: bool=False) -> str:
    decoration = ""
    if bold:
        decoration += "1;"
    if underline:
        decoration += "4;"
    return decoration


# Automatically gets data from CyberPatriot ReadMe

import urllib.request

def get_readme_data() -> str:
    fp = urllib.request.urlopen("") #README url here
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

# Todo finish this function
def parse_readme_data(data: str) -> None:
    my_list = data.splitlines()
    users = []
