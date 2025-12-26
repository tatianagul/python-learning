import json
from pathlib import Path


def load_file(path: Path) -> list:
    if path.exists():
        with open(path, "r") as f:
            expenses_data = json.load(f)
    else:
        with open(path, "w") as f:
            expenses_data = []
            json.dump(expenses_data, f)
    return expenses_data


def save_expenses(expenses_data: list[dict], path: Path):
    with open(path, "w")as f:
        json.dump(expenses_data, f, indent=1)
