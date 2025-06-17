import requests
from bs4 import BeautifulSoup
import time
import csv

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36"
}

BASE_URL = "https://www.olx.uz/transport/legkovye-avtomobili/"
OUTPUT_FILE = "olx_clean_data.csv"


def clean_text(text):
    return text.replace("\n", "").replace("\t", "").strip()


def scrape_page(page=1):
    url = f"{BASE_URL}?page={page}"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.select("div[data-cy='l-card']")

    data = []

    for card in cards:
        title_tag = card.select_one("h6")
        price_tag = card.select_one("p[data-testid='ad-price']")
        location_tag = card.select_one("p[data-testid='location-date']")
        link_tag = card.select_one("a")

        if title_tag and price_tag and location_tag and link_tag:
            full_link = "https://www.olx.uz" + link_tag.get("href", "")
            location_parts = location_tag.text.strip().split(" - ")
            location = location_parts[0] if len(location_parts) > 0 else ""
            date = location_parts[1] if len(location_parts) > 1 else ""

            data.append({
                "title": clean_text(title_tag.text),
                "price": clean_text(price_tag.text),
                "location": clean_text(location),
                "date": clean_text(date),
                "url": full_link
            })

    return data


def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "location", "date", "url"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    all_data = []
    for page in range(1, 4):  # 1-3 sahifalar uchun
        print(f"[+] Sahifa {page} olinmoqda...")
        page_data = scrape_page(page)
        all_data.extend(page_data)
        time.sleep(2)  # Saytni haddan tashqari zo'riqtirmaslik uchun

    save_to_csv(all_data, OUTPUT_FILE)
    print(f"[✔] {len(all_data)} ta e'lon '{OUTPUT_FILE}' fayliga saqlandi.")


if __name__ == "__main__":
    main()
