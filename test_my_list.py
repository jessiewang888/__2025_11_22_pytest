# test_my_list.py
import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("a")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("b")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("c")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").first.check()
    page.get_by_role("listitem").filter(has_text="b").get_by_label("Toggle Todo").check()
    page.get_by_role("checkbox", name="Toggle Todo").nth(2).check()
    page.get_by_text("Mark all as complete").click()
    page.get_by_role("link", name="Active").click()
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("link", name="All").click()
    page.get_by_role("button", name="Delete").click()
    page.get_by_role("button", name="Delete").click()
    page.get_by_role("button", name="Delete").click()