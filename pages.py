# pages.py
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://example.com")
    page.screenshot(path="example-screenshot.png")
    new_page = context.new_page()
    new_page.goto("https://playwright.dev/python/docs/api/class-page")
    new_page.screenshot(path="doc.png")
    page.locator("css=a").click()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
