import time
import logging

from wiki import fetch_deaths
from article import fetch_intro
from storage import load, save
from notifier import notify

from config import WIKI_URL as URL, CHECK_INTERVAL_SECONDS

logging.basicConfig(level=logging.INFO)

def main():
    sent = load()

    while True:
        logging.info("Checking wiki...")
        records = fetch_deaths(URL)
        logging.info(f"Parsed {len(records)} records")

        for r in records:
            if r["name"] in sent:
                continue

            intro = fetch_intro(r["url"])
            notify(r["name"], r["url"], intro)

            sent.add(r["name"])
            save(sent)

        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
