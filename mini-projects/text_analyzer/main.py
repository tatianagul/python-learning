from pathlib import Path
from extractor import extract_emails, extract_phones, extract_dates, extract_urls


def main():
    text_file = Path("data/sample.txt")

    emails = extract_emails(text_file)
    phones = extract_phones(text_file)
    dates = extract_dates(text_file)
    urls = extract_urls(text_file)

    print("📧 Emails:")
    for email in emails:
        print(f" - {email}")

    print("\n📞 Phones:")
    for phone in phones:
        print(f" - {phone}")

    print("\n📅 Dates:")
    for date in dates:
        print(f" - {date}")

    print("\n🌐 URLs:")
    for url in urls:
        print(f" - {url}")


if __name__ == "__main__":
    main()
