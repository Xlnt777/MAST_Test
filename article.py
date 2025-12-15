import re
import requests
from bs4 import BeautifulSoup
from config import HEADERS


def clean(text: str) -> str:
    text = re.sub(r"\[[^\]]+]", "", text)

    text = text.replace("́", "")

    text = text.replace("\xa0", " ")

    text = re.sub(r"\s+([,.;:])", r"\1", text)

    text = re.sub(r"\(\s+", "(", text)

    text = re.sub(r"\s+\)", ")", text)

    text = re.sub(r"\s*—\s*", " — ", text)

    text = re.sub(r"[ ]{2,}", " ", text)

    return text.strip()

def fetch_intro(url: str) -> str:
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
    except requests.RequestException:
        return ""

    if r.status_code != 200:
        return ""

    soup = BeautifulSoup(r.text, "html.parser")
    parser_output = soup.select_one("div.mw-parser-output")
    if not parser_output:
        return ""

    for p in parser_output.find_all("p"):
        text = p.get_text(" ", strip=True)  
        if text:
            return clean(text)

    return ""
