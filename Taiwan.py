from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://qa-practice.razvanvancea.ro/dropdowns.html")

    # Wait for the loader to disappear (display: none)
    page.locator("#dropdown-menu").select_option("Taiwan")
        page.locator.select_option(delay=1000)
    

    #print("Loader disappeared!")

    #browser.close()
