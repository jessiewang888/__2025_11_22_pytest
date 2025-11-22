# drag.py
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    )
    page = context.new_page()

    page.goto("https://tw.yahoo.com", timeout=0)
    time.sleep(2)
    page.locator('xpath=/html/body/div[2]/div/div/div[2]/div/nav/div[1]/ul/li[1]/a/div').hover()
    page.mouse.down()

    search_input = page.locator("xpath=/html/body/div[2]/div/header/div/div/div/div[1]/div[1]/div/div/form/input[1]")
    box = search_input.bounding_box()
    page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
    search_input.hover()
    page.mouse.up()

    time.sleep(10)
    browser.close()





