# loading.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://qa-practice.razvanvancea.ro/loader.html")

    # Wait for the loader to disappear (display: none)
    page.locator("#loader").wait_for(state="hidden")

    print("Loader disappeared!")

    browser.close()
