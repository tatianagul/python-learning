from decorators import dec_command
from datetime import datetime


@dec_command("time", "Show current time")
def time_cmd(args):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {now}")
