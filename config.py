# ===== Wikipedia =====
WIKI_URL = "https://ru.wikipedia.org/wiki/Умершие_в_августе_2023_года"

USER_AGENT = "WikiDeathsWatcher/1.0 (test task; contact: your_email@example.com)"

HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
}

CHECK_INTERVAL_SECONDS = 60

# ===== Email / SMTP =====
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USE_TLS = True

SMTP_USERNAME = "your_email@gmail.com"
SMTP_PASSWORD = "your_app_password"

EMAIL_FROM = "your_email@gmail.com"
EMAIL_TO = ["receiver@example.com"]


# ===== Runtime =====
DEBUG = "True"