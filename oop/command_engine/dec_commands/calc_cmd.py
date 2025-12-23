from decorators import dec_command


@dec_command("calc", "Calculete simple expression (e.g. 2+3*4)")
def calc_cmd(args):
    if not args:
        print("Usage: /calc <expression>")
        return

    expression = "".join(args)

    try:
        result = eval(expression, {"__builtins__": {}})
    except Exception:
        print("Invalid expression")
        return

    print(f"Result: {result}")
