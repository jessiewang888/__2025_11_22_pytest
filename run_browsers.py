# run_browsers.py
import time
import pathlib
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    p = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    browser = chromium.launch(headless=False, executable_path=p)
    page = browser.new_page()
    page.goto("https://example.com")
    time.sleep(10)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
