from pathlib import Path
import re

from patterns import email_pattern, phone_pattern


def extract_emails(text_file: Path):
    with text_file.open("r", encoding="utf-8") as file:
        content = file.read()
        email_list = set(re.findall(email_pattern, content))
    return sorted(email_list)


def normalize_phone(raw_phone):
    normalized = str(raw_phone)
    normalized = normalized.replace(" ", "")
    normalized = normalized.replace("-", "")
    normalized = normalized.replace("(", "")
    normalized = normalized.replace(")", "")
    return normalized


def is_valid_phone(phone: str) -> bool:
    if len(phone) == 0:
        return False

    if phone.startswith("+"):
        if not phone[1:].isdigit():
            return False
        n = len(phone[1:])
        if n < 10 or n > 15:
            return False

    elif phone.isdigit():
        n = len(phone)
        if n < 10 or n > 15:
            return False

    else:
        return False

    return True


def extract_phones(text_file: Path):
    phone_list = set()
    with text_file.open("r", encoding="utf-8") as file:
        for line in file:
            matches = re.findall(phone_pattern, line)
            for raw_phone in matches:
                normalized = normalize_phone(raw_phone)
                if is_valid_phone(normalized):
                    phone_list.add(normalized)
    return sorted(phone_list)
