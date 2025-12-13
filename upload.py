# upload.py
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.compress2go.com/create-zip-file")
    time.sleep(2)
    with page.expect_file_chooser() as fc_info:
        page.get_by_text("Choose File").click()

    file_chooser = fc_info.value
    file_chooser.set_files("/tmp/down.csv")
    page.locator("#submitBtn").click()

     with page.expect_download() as download_info:
        # Perform the action that initiates download
        page.locator("#content > div.file-container > div:nth-child(3) > div > div.flex-grow-1.justify-content-end.d-flex.file-actions.item.align-items-center.flex-wrap > div:nth-child(2) > a", name="CSV").click()
    download = download_info.value
    download.save_as("/Users/user/Downloads" + "new1.csv")

    time.sleep(10)
    browser.close()
