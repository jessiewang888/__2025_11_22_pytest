# locators.py
import time
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa-practice.razvanvancea.ro/checkboxes.html")
    print(page.get_by_role("checkbox").all(), len(page.get_by_role("checkbox").all()))
    for locator in page.get_by_role("checkbox").all():
        time.sleep(2)
        locator.check()
    time.sleep(2)
    page.get_by_text("Reset").click()
    time.sleep(10)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)