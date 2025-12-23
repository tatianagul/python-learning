from router import route_command

import dec_commands.calc_cmd
import dec_commands.help_cmd
import dec_commands.time_cmd
import dec_commands.random_cmd


def main():
    print("Command Engine started. Type /help for commands.")

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue

        if user_input == "/exit":
            print("Bye!")
            break

        if not user_input.startswith("/"):
            print("Commands must start with "/"")
            continue

        parts = user_input[1:].split()
        command_name = parts[0]
        args = parts[1:]

        try:
            route_command(command_name, args)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
