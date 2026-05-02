import os
from templates import FOLDERS, FILES


def create_project(base_path):
    for folder in FOLDERS:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    for file_path, content in FILES.items():
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
