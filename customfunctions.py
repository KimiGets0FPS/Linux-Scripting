import os
import subprocess



def _get_command(command: str) -> list[str]:
    return command.split(" ")

def run_command(command: str) -> None:
    subprocess.run(_get_command(command), capture_output=True, text=True)

def run_commands(commands: list[str]) -> None:
    for i in range(len(commands)):
        run_command(commands[i])

def clear():
    os.system("clear")
    exit(1)

# DECORATION

def print_green(string: str) -> None:
    print(f"\033[92m{string}\033[0m")

def print_yellow(string: str) -> None:
    print(f"\033[93m{string}\033[0m")

def print_red(string: str) -> None:
    print(f"\033[91m{string}\033[0m")

def print_blue(string: str) -> None:
    print(f"\033[94m{string}\033[0m")


def main():
    ...

if __name__ == "__main__":
    main()
