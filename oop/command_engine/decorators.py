from registry import register_command


def dec_command(name, description=""):
    def decorator(func):
        register_command(name, func, description)
        return func
    return decorator
