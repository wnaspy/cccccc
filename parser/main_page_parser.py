from bs4 import BeautifulSoup

def parse_main_page(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, 'lxml')

def find_volumes(soup: BeautifulSoup):
    volumes = []
    index = 1
    while True:
        vol_tag = soup.select_one(f"#volume_{index} > .sect-title")
        if not vol_tag:
            break
        volumes.append((index, vol_tag.text.strip()))
        index += 1
    return volumes

def find_chapters_for_volume(soup: BeautifulSoup, volume_index: int):
    # nth-child starts at 1, volume-list starts at 3 for volume 1
    nth = volume_index + 2
    selector = f".volume-list:nth-child({nth}) > .d-lg-block li"
    return soup.select(selector)
