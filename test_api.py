from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:8000"
    )
    yield request_context
    request_context.dispose()

def create_test_item(api_request_context: APIRequestContext) -> int:
    response = api_request_context.post("/items", data={
        "name": "Temp Item",
        "description": "Temporary for testing"
    })
    # 4xx, 404, 500, 422
    assert response.ok
    assert response.status == 200
    return response.json()["id"]

def test_create_item(api_request_context: APIRequestContext):
    response = api_request_context.post("/items", data={
        "name": "Test Create",
        "description": "Creating an item"
    })
    assert response.ok
    data = response.json()
    assert data["name"] == "Test Create"
    assert data["description"] == "Creating an item"
    assert response.status ==201

def test_read_item(api_request_context: APIRequestContext):
    item_id = create_test_item(api_request_context)
    response = api_request_context.get(f"/items/{item_id}")
    assert response.ok
    assert response.status ==200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Temp Item"
    assert data["description"] == "Temporary for testing"

def test_update_item(api_request_context: APIRequestContext):
    item_id = create_test_item(api_request_context)
    response = api_request_context.patch(f"/items/{item_id}", data={
        "name": "Updated Name",
        "description": "Updated Description"
    })
    assert response.ok
    response = api_request_context.get(f"/items/{item_id}")
    assert response.ok
    data = response.json()
    assert data["description"] == "Updated Description"

def test_update_item_cannot_modify_name_with_description(api_request_context: APIRequestContext):
    item_id = create_test_item(api_request_context)
    response = api_request_context.patch(f"/items/{item_id}", data={
        "name": "Updated Name",
        "description": "Updated Description"
    })
    assert response.ok
    response = api_request_context.get(f"/items/{item_id}")
    assert response.ok
    data = response.json()
    assert data["description"] == "Updated Description"
    assert data["name"] == "Temp Item"

def test_update_item_cannot_modify_name(api_request_context: APIRequestContext):
    item_id = create_test_item(api_request_context)
    response = api_request_context.patch(f"/items/{item_id}", data={
        "name": "Updated Name"
    })
    assert not response.ok
    response = api_request_context.get(f"/items/{item_id}")
    assert response.ok
    data = response.json()
    assert data["name"] == "Temp Item" 

def test_delete_item(api_request_context: APIRequestContext):
    item_id = create_test_item(api_request_context)
    response = api_request_context.delete(f"/items/{item_id}")
    assert response.ok
    assert response.status == 204
    assert response.body() == ""
    # Verify it's deleted
    response = api_request_context.get(f"/items/{item_id}")
    assert response.status == 404


def test_get_not_exists_item_will_return_404(api_request_context: APIRequestContext):
    item_id = create_test_item(api_request_context)
    response = api_request_context.get(f"/items/{item_id + 1}")
    assert response.status == 404

def test_get_not_exists_string_id_item_will_return_422(api_request_context: APIRequestContext):
    response = api_request_context.get("/items/osidjfospidfj-sd89fjspoifjsdfpoisjf-")
    assert response.status == 422


def test_update_not_exists_item_will_return_404(api_request_context: APIRequestContext):
    item_id = create_test_item(api_request_context)
    response = api_request_context.patch(f"/items/{item_id + 1}", data={
        "name": "Updated Name",
        "description": "Updated Description"
    })
    assert response.status == 404


def test_delete_not_exists_item_will_return_404(api_request_context: APIRequestContext):
    item_id = create_test_item(api_request_context)
    response = api_request_context.delete(f"/items/{item_id}")
    assert response.ok
    response = api_request_context.delete(f"/items/{item_id}")
    assert response.ok


# @pytest.fixture(autouse=True)
# def db():
#     # create DB
#     yield
#     # delete DB
