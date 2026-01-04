from pathlib import Path
from extractor import extract_emails, extract_phones, extract_dates, extract_urls


text_file = Path("data/sample.txt")


print(extract_emails(text_file))
print()
print(extract_phones(text_file))
print()
print(extract_dates(text_file))
print()
print(extract_urls(text_file))
