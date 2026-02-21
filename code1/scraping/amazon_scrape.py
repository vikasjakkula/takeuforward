import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.in/s?k=hoodies"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")

titles = soup.select("span.a-size-medium.a-color-base.a-text-normal")

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Product Title"])
    for t in titles:
        writer.writerow([t.text.strip()])

print("Done! Data saved to products.csv")
