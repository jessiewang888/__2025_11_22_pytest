# locators.py
import time
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa-practice.razvanvancea.ro/checkboxes.html")
    page.locator("#checkbox1").click() # CSS selector
    time.sleep(2)
    page.locator("//html/body/div/div/form/div/div[2]/input").click() # xpath
    '//*[@id="checkbox2"]'
    time.sleep(2)
    for locator in page.get_by_role("checkbox").all():
        # locator.check()
        locator.click(delay=1000)
    time.sleep(2)
    page.get_by_text("Reset").click()
    time.sleep(10)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
