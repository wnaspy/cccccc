import os
import re

def clean_name(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def save_text_file(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
