"""
scraper.py - InterNACHI Gallery Image Scraper
Released to the Public Domain under The Unlicense (https://unlicense.org/)

Author: Kanawha IT Security LLC (https://kitswv.com)
Contact: tim@kitswv.com

Portions of this script generated with assistance from OpenAI's ChatGPT.

This script logs into InterNACHI, navigates to the Image Gallery, scrapes
all category links, and downloads all images into a local folder.

NO WARRANTY — USE AT YOUR OWN RISK.
"""

from playwright.sync_api import sync_playwright
import os
import requests
from urllib.parse import urljoin, urlparse

USERNAME = "tim@kitswv.com"
PASSWORD = "AnM!6sh0tRugburn69"
LOGIN_URL = "https://www.nachi.org/login"
GALLERY_URL = "https://www.nachi.org/gallery"
OUTPUT_DIR = "downloaded_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_image(img_url):
    filename = os.path.join(OUTPUT_DIR, os.path.basename(urlparse(img_url).path))
    if not os.path.exists(filename):
        response = requests.get(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✅ Downloaded: {filename}")
        else:
            print(f"❌ Failed to download {img_url}")
    else:
        print(f"✔️ Already exists: {filename}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    print("🔐 Logging into InterNACHI...")
    page.goto(LOGIN_URL)
    page.fill('input[name="username"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')
    print("✅ Logged in.")

    print("🧭 Navigating to Gallery page...")
    page.goto(GALLERY_URL)
    page.wait_for_load_state('networkidle')

    links = page.query_selector_all('a[href^="https://www.nachi.org/gallery/"]')
    category_links = set()
    for link in links:
        href = link.get_attribute('href')
        if "/gallery/" in href and href != GALLERY_URL:
            category_links.add(href)

    print(f"✅ Found {len(category_links)} gallery category pages.")

    for cat_url in category_links:
        print(f"🔎 Processing category: {cat_url}")
        page.goto(cat_url)
        page.wait_for_load_state('networkidle')

        images = page.query_selector_all('img')
        for img in images:
            src = img.get_attribute('src')
            if src and ("nachi.org" in src or "cloudinary.com" in src):
                img_url = urljoin(cat_url, src)
                download_image(img_url)

    print("✅ All gallery images downloaded successfully.")
    browser.close()
