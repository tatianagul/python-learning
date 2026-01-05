from decorators import dec_command
import random


@dec_command("random", "Generate random number between min and max")
def random_cmd(args):
    if len(args) != 2:
        print("Usage: /random <min> <max>")
        return

    try:
        min_val = int(args[0])
        max_val = int(args[1])
    except ValueError:
        print("Arguments must be integers")
        return

    print(f"Random number: {random.randint(min_val, max_val)}")
