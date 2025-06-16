from utils.url_utils import validate_url, extract_slug, remove_numeric_prefix
from utils.file_utils import clean_name, ensure_dir, save_text_file
from utils.request_utils import fetch_url
from parser.main_page_parser import parse_main_page, find_volumes, find_chapters_for_volume
from parser.chapter_parser import is_illustration, extract_chapter_info, fetch_chapter_content

def main(url):
    validate_url(url)
    slug_raw = extract_slug(url)
    slug = remove_numeric_prefix(slug_raw)
    folder = f"data/{clean_name(slug)}"
    ensure_dir(folder)

    html = fetch_url(url)
    soup = parse_main_page(html)
    volumes = find_volumes(soup)

    for vol_index, vol_name in volumes:
        vol_folder = f"{folder}/{clean_name(vol_name)}"
        ensure_dir(vol_folder)
        chapters_li = find_chapters_for_volume(soup, vol_index)

        for li in chapters_li:
            chap_name, chap_href = extract_chapter_info(li)
            if not chap_name or not chap_href:
                continue
            if is_illustration(chap_name):
                print(f"Skip minh họa: {chap_name}")
                continue
            chap_url = chap_href if chap_href.startswith("http") else "https://docln.net" + chap_href
            content = fetch_chapter_content(chap_url)
            if content:
                filename = f"{clean_name(chap_name)}.txt"
                save_text_file(f"{vol_folder}/{filename}", content)
                print(f"Saved {filename}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py <url_truyen>")
        sys.exit(1)
    main(sys.argv[1])
