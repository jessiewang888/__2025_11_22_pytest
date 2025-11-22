# run_browsers.py
import time
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    firefox = playwright.firefox
    # headed==headless=False
    # browser = firefox.launch(headless=True)
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    time.sleep(10)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
