import re

def validate_url(url: str):
    if not re.match(r"^https?://", url):
        raise ValueError("URL phải bắt đầu bằng http hoặc https")

def extract_slug(url: str) -> str:
    m = re.search(r"https?://docln\.net/truyen/([a-zA-Z0-9_-]+)", url)
    if not m:
        raise ValueError("URL không hợp lệ, ví dụ đúng: https://docln.net/truyen/slug")
    return m.group(1)

def remove_numeric_prefix(slug: str) -> str:
    parts = slug.split("-", 1)
    if len(parts) == 2 and parts[0].isdigit():
        return parts[1]
    return slug
