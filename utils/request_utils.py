import requests

def fetch_url(url: str) -> str:
    r = requests.get(url)
    r.raise_for_status()
    return r.text
