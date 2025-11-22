# locators.py
import time
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa-practice.razvanvancea.ro/radiobuttons.html")
    for locator in page.get_by_role("radio").all()[:-1]:
        # locator.check()
        locator.click(delay=1000)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
