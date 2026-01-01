from pathlib import Path
import re

from patterns import email_pattern


def extract_emails(text_file: Path):
    with text_file.open("r", encoding="utf-8") as file:
        content = file.read()
        email_list = set(re.findall(email_pattern, content))
    return sorted(email_list)
