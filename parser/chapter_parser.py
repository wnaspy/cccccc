from bs4 import BeautifulSoup
from utils.request_utils import fetch_url

def is_illustration(chap_name: str) -> bool:
    lower = chap_name.lower()
    return "minh họa" in lower or "minh họa" in lower

def extract_chapter_info(li) -> tuple:
    chap_name_tag = li.select_one(".chapter-name")
    chap_link_tag = li.select_one("a")
    if not chap_name_tag or not chap_link_tag:
        return None, None
    return chap_name_tag.text.strip(), chap_link_tag.get("href")

def fetch_chapter_content(chap_url: str) -> str:
    html = fetch_url(chap_url)
    soup = BeautifulSoup(html, 'lxml')
    # Lấy tất cả thẻ có id là số (vd id="1", id="31", id="150", ...)
    number_tags = [tag for tag in soup.find_all(attrs={"id": True}) if tag["id"].isdigit()]
    parts = [tag.get_text(separator="\n", strip=True) for tag in number_tags if tag.get_text(strip=True)]
    return "\n\n".join(parts)
