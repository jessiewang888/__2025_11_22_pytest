# test_shopping.py
import re
from playwright.sync_api import Page, expect


def test_shop_pricing(page: Page):
    page.goto("https://qa-practice.razvanvancea.ro/products_list.html")
    locator = page.get_by_role("button", name="ADD TO CART").first
    locator.scroll_into_view_if_needed()
    locator.click(delay=1000)
    locator = page.get_by_role("button", name="ADD TO CART").nth(1)
    locator.scroll_into_view_if_needed()
    locator.click(delay=1000)

    locator = page.get_by_role("button", name="PURCHASE")
    locator.scroll_into_view_if_needed()
    locator.click(delay=1000)
    expect(page.locator('//*[@id="message"]/b')).to_have_text(re.compile(r"\$1142.11"))
