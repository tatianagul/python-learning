from zipfile import ZipFile
from pathlib import Path


def backup_to_zip(data_path: Path, backup_path: Path):
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(backup_path, mode="w") as zip_backup:
        for file in data_path.iterdir():
            if file.is_file():
                zip_backup.write(file, arcname=file.name)
