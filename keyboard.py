# keyboard.py
import time
from playwright.sync_api import sync_playwright
url = "https://docs.google.com/spreadsheets/d/1BuPFilvSDtfH7DB0Tvy8_0FQ9mOnPKjZNjWu6B-Oqsk/edit?gid=1757601524#gid=1757601524"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    time.sleep(2)
    for _ in range(10):
        page.keyboard.press("Enter")
        page.keyboard.type("Hello World!")
        page.keyboard.press("Enter")
    time.sleep(2)

    for _ in range(10):
        page.keyboard.press("ArrowUp")

    time.sleep(2)
    page.keyboard.down("Shift")
    for _ in range(10):
        page.keyboard.press("ArrowDown")
        time.sleep(2)
    page.keyboard.up("Shift")
    page.keyboard.press("Delete")
    time.sleep(10)
    browser.close()
