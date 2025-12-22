from registry import get_commands


def route_command(command_name, args):
    commands = get_commands()

    if command_name not in commands:
        raise ValueError(f"Unknown cmmand: {command_name}")

    command_func = commands[command_name]["function"]
    command_func(args)
