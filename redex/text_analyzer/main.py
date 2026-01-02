from pathlib import Path
from extractor import extract_emails, extract_phones


text_file = Path("data/sample.txt")


print(extract_emails(text_file))
print()
print(extract_phones(text_file))
