# download.py
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://data.gov.tw/dataset/137743")
    time.sleep(2)

    with page.expect_download() as download_info:
        # Perform the action that initiates download
        page.get_by_role("button", name="CSV").click()
    download = download_info.value
    download.save_as("/tmp/" + "down.csv")
    # C:\\tmp\down.csv


    time.sleep(10)
    browser.close()
