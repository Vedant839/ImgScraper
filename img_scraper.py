import os, requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

site = "https://www.wikipedia.org/" # replace this with other website link
folder = "images"
os.makedirs(folder, exist_ok=True)

for img in BeautifulSoup(requests.get(site).text, "html.parser").find_all("img"):
    url = urljoin(site, img.get("src", ""))
    with open(f"{folder}/{url.split('/')[-1]}", "wb") as f:
        f.write(requests.get(url).content)
        