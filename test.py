#test
import re
from playwright.sync_api import Page, expect
import pytest


def create_todo_item(page, todo_text: str):
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill(todo_text)
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")


def test_second_todo_in_list(page: Page):
    # 新增兩個項目到列表
    page.goto("https://demo.playwright.dev/todomvc/#/")
    todo_input =  page.get_by_role("textbox", name="What needs to be done?")
    create_todo_item(page, "xxxxx")
    expect(page.get_by_test_id("todo-title")).to_contain_text("xxxxx")
    create_todo_item(page, "test2")
    expect(page.locator("body")).to_contain_text("test2")

@pytest.fixture
def create_and_check(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    create_todo_item(page, "test todo")
    page.get_by_role("checkbox", name="Toggle Todo").check()


def test_checked_item_in_all_list(page: Page, create_and_check) -> None:
    expect(page.get_by_test_id("todo-title")).to_contain_text("test todo")


def test_checked_item_in_completed_list(page: Page, create_and_check) -> None:
    page.get_by_role("link", name="Completed").click()
    expect(page.get_by_test_id("todo-title")).to_contain_text("test todo")
    # page.get_by_role("link", name="Active").click()


def test_checked_item_not_in_active_list(page: Page, create_and_check) -> None:
    page.get_by_role("link", name="Active").click()
    # 不顯示
    expect(page.locator("html")).not_to_contain_text("test todo")


def test_removed_item_not_in_all_list(page: Page, create_and_check) -> None:
    page.get_by_role("button", name="Clear completed").click()
    # 不顯示
    expect(page.locator("html")).not_to_contain_text("test todo")


def test_removed_item_not_in_active_list(page: Page, create_and_check) -> None:
    page.get_by_role("link", name="Active").click()
    page.get_by_role("button", name="Clear completed").click()
    # 不顯示
    expect(page.locator("html")).not_to_contain_text("test todo")


def test_removed_item_not_in_completed_list(page: Page, create_and_check) -> None:
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("button", name="Clear completed").click()
    # 不顯示
    expect(page.locator("html")).not_to_contain_text("test todo")


def test_check_all_button(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    for _ in range(10):
        create_todo_item(page, "test todo")
    page.locator("body > section > div > section > label").click()

    count = 0
    for item_locator in page.locator("xpath=/html/body/section/div/section/ul/li/div/input").all():
        expect(item_locator).to_be_checked()
        count += 1
    assert count == 10


def test_checked_item_will_not_be_affected_by_check_all_when_unchecked_item_exists(page: Page, create_and_check) -> None:
    create_todo_item(page, "xxxxx")
    check_all_button = page.locator("body > section > div > section > label")
    check_all_button.click()
    count = 0
    for item_locator in page.locator("xpath=/html/body/section/div/section/ul/li/div/input").all():
        expect(item_locator).to_be_checked()
        count += 1
    assert count == 2
