COMMAND_REGISTRY = {}


def register_command(name, func, description=""):
    COMMAND_REGISTRY[name] = {
        "function": func,
        "description": description
    }


def get_commands():
    return COMMAND_REGISTRY


print(COMMAND_REGISTRY)
