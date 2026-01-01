from pathlib import Path
import re

text_file = Path("data/sample.txt")

email_pattern = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9-.]+\.[a-zA-Z]+"


with text_file.open("r", encoding="utf-8") as file:
    content = file.read()
    find_email = set(re.findall(email_pattern, content))
    print(sorted(find_email))
