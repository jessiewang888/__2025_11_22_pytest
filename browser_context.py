# browser_context.py
import re
import time
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto("https://qa-practice.razvanvancea.ro/auth_ecommerce.html")
    page.get_by_placeholder("Enter email - insert admin@").click()
    page.get_by_placeholder("Enter email - insert admin@").fill("admin@admin.com")
    page.get_by_placeholder("Enter email - insert admin@").press("Tab")
    page.get_by_placeholder("Enter Password - insert").fill("admin123")
    page.get_by_placeholder("Enter Password - insert").press("Enter")
    time.sleep(3)
    new_context = browser.new_context()
    page = new_context.new_page()
    page.goto("https://qa-practice.razvanvancea.ro/auth_ecommerce.html")
    time.sleep(10)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
