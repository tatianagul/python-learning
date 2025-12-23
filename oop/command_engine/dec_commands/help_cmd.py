from decorators import dec_command
from registry import get_commands


@dec_command("help", "Show available commands")
def help_cmd(args):
    commands = get_commands()

    print("Available commands:")
    for name, data in commands.items():
        print(f"/{name} - {data["description"]}")
