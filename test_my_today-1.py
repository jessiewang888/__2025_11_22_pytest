import re
import time
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture
def page(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("1111")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()
    return page

def goto_tab(page: Page, tab: str):
    page.get_by_role("link", name=tab).click()
    expect(page.get_by_role("link", name=tab)).to_contain_class("selected")

# checked item in all page
@pytest.mark.parametrize("tab", ["All", "Completed"])
def test_checked_item_in_list(page: Page, tab: str):
    goto_tab(page, tab)
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text("my items")

def test_checked_item_not_in_active_list(page: Page):
    goto_tab(page, "Active")
    expect(page.get_by_test_id("todo-title")).to_be_visible(visible=False)

   