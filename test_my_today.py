import re
import time
from playwright.sync_api import Page, expect
import pytest


@pytest.fixture
def create_and_check(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("my items")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()
    

def goto_tab(page: Page, tab: str):
    page.get_by_role("link", name=tab).click()
    expect(page.get_by_role("link", name=tab)).to_contain_class("selected")

# checked item in all page
@pytest.mark.parametrize("tab", ["All", "Completed"])
def test_checked_item_in_list(page: Page, tab: str, create_and_check):
    goto_tab(page, tab)
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text("my items")


def test_checked_item_not_in_active_list(page: Page, create_and_check):
    goto_tab(page, "Active")
    expect(page.get_by_test_id("todo-title")).to_be_visible(visible=False)

@pytest.mark.parametrize("tab", ["All", "Completed", "Active"])
def test_no_completed_items_removed_item_not_in_all_tabs(page: Page, tab: str):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("test")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    goto_tab(page, tab)
    expect(page.get_by_role("button", name="Clear completed")).to_be_visible(visible=False)

@pytest.mark.parametrize("tab", ["All", "Completed", "Active"])
def test_remove_item_in_all_tabs(page: Page, tab: str, create_and_check):
    goto_tab(page, tab)
    page.get_by_role("button", name="Clear completed").click()
    expect(page.get_by_test_id("todo-title")).to_be_visible(visible=False)

def test_checked_item_not_in_active_list(page: Page, create_and_check):
    goto_tab(page, "Active")
    expect(page.get_by_test_id("todo-title")).to_be_visible(visible=False)


@pytest.mark.parametrize("tab", ["All", "Completed", "Active"])
def test_no_completed_items_removed_item_not_in_all_tabs(page: Page, tab: str):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("test")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    goto_tab(page, tab)
    expect(page.get_by_role("button", name="Clear completed")).to_be_visible(visible=False)


@pytest.mark.parametrize("tab", ["All", "Completed", "Active"])
def test_remove_item_in_all_tabs(page: Page, tab: str, create_and_check):
    goto_tab(page, tab)
    page.get_by_role("button", name="Clear completed").click()
    expect(page.get_by_test_id("todo-title")).to_be_visible(visible=False)


# check all button
def test_check_all_button(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("test1")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("test2")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_text("Mark all as complete").click()
    expect(page.get_by_role("listitem").filter(has_text="test1").get_by_label("Toggle Todo")).to_be_checked()
    expect(page.get_by_role("listitem").filter(has_text="test2").get_by_label("Toggle Todo")).to_be_checked()

# check all button -> 1 checked -> not affect
def test_checked_item_will_not_be_affected_by_check_all_when_unchecked_item_exists(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("test")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("test2")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").first.check()
    page.get_by_text("Mark all as complete").click()
    expect(page.get_by_role("checkbox", name="Toggle Todo").first).to_be_checked()
    expect(page.get_by_role("listitem").filter(has_text="test2").get_by_label("Toggle Todo")).to_be_checked()

# uncheck all
def test_uncheck_all_button(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("test1")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("test2")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_text("Mark all as complete").click()
    expect(page.get_by_role("listitem").filter(has_text="test1").get_by_label("Toggle Todo")).to_be_checked()
    expect(page.get_by_role("listitem").filter(has_text="test2").get_by_label("Toggle Todo")).to_be_checked()
    page.get_by_text("Mark all as complete").click()
    # .not_to_be_checked()
    expect(page.get_by_role("listitem").filter(has_text="test1").get_by_label("Toggle Todo")).not_to_be_checked()
    expect(page.get_by_role("listitem").filter(has_text="test2").get_by_label("Toggle Todo")).not_to_be_checked()


# checked will reduce counter
def test_checked_will_reduce_counter(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("test")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("testmexx")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    expect(page.locator("body > section > div > footer > span > strong")).to_contain_text("2")
    page.get_by_role("listitem").filter(has_text="testmexx").get_by_label("Toggle Todo").check()
    expect(page.locator("body > section > div > footer > span > strong")).to_contain_text("1")


# delete will reduce counter
def test_delete_will_reduce_counter(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("test")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("testmexx")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    expect(page.locator("body > section > div > footer > span > strong")).to_contain_text("2")
    # delete
    # hover li
    page.locator("body > section > div > section > ul > li:nth-child(1)").hover()
    # delete
    page.locator("body > section > div > section > ul > li:nth-child(1) > div > button").click()
    expect(page.locator("body > section > div > footer > span > strong")).to_contain_text("1")

# checked and deleted will not affect
def test_delete_checked_item_will_not_affect_counter(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("test")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("testmexx")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    expect(page.locator("body > section > div > footer > span > strong")).to_contain_text("2")
    page.get_by_role("listitem").filter(has_text="testmexx").get_by_label("Toggle Todo").check()
    expect(page.locator("body > section > div > footer > span > strong")).to_contain_text("1")
    # delete
    # hover li
    page.locator("body > section > div > section > ul > li:nth-child(2)").hover()
    # delete
    page.locator("body > section > div > section > ul > li:nth-child(2) > div > button").click()
    expect(page.locator("body > section > div > footer > span > strong")).to_contain_text("1")