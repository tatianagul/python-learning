from pathlib import Path
from extractor import extract_emails


text_file = Path("data/sample.txt")


print(extract_emails(text_file))
