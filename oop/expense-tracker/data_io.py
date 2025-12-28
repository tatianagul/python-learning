import json
from pathlib import Path


def load_file(path: Path) -> list[dict]:
    if not path.exists():
        with open(path, "w") as f:
            json.dump([], f)
        return []

    try:
        with open(path, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        print("Warning: expenses.json is empty or corrupted. Starting with empty list.")
        with open(path, "w") as f:
            json.dump([], f)
        return []

    except OSError:
        print("Warning: Could not read expenses file. Starting with empty list.")
        return []


def save_expenses(expenses_data: list[dict], path: Path):
    with open(path, "w")as f:
        json.dump(expenses_data, f, indent=1)
