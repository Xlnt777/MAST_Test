import json
from pathlib import Path

PATH = Path("data/sent.json")

def load():
    if not PATH.exists():
        return set()
    return set(json.loads(PATH.read_text(encoding="utf-8")))

def save(items):
    PATH.parent.mkdir(exist_ok=True)
    PATH.write_text(
        json.dumps(sorted(items), ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
