from pathlib import Path
import re

from patterns import email_pattern, phone_pattern


def extract_emails(text_file: Path):
    with text_file.open("r", encoding="utf-8") as file:
        content = file.read()
        email_list = set(re.findall(email_pattern, content))
    return sorted(email_list)


def extract_phones(text_file: Path):
    phone_list = set()
    with text_file.open("r", encoding="utf-8") as file:
        for line in file:
            matches = re.findall(phone_pattern, line)
            phone_list.update(matches)
    return sorted(phone_list)
