import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import HEADERS

BASE = "https://ru.wikipedia.org"

def fetch_deaths(url: str) -> list[dict]:
    try:
        response = requests.get(url, headers=HEADERS, timeout=20)
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return []

    if response.status_code != 200:
        logging.warning(f"Wiki returned {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    records = []

    for li in soup.select("div.mw-parser-output ul > li"):
        text = li.get_text(strip=True)

        if "—" not in text:
            continue

        a = li.find("a", href=True)
        if not a:
            continue

        name = a.get_text(strip=True)

        if a["href"].startswith("/wiki/"):
            link = urljoin(BASE, a["href"])
        else:
            ext = li.select_one("a.extiw")
            if not ext:
                continue
            link = ext["href"]

        records.append({
            "name": name,
            "url": link
        })

    logging.info(f"Parsed {len(records)} records from wiki")
    return records
