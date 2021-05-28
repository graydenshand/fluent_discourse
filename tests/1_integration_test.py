from conf_tests import BASE_URL, client
import pytest
import os
from fluent_discourse import *


@pytest.mark.integration
def test_get_latest(client):
    # Tests a get request
    latest = client.latest.json.get()
    assert latest is not None
    assert "users" in latest.keys()
    assert "topic_list" in latest.keys()


@pytest.mark.integration
def test_log_out_user(client):
    # Tests a put request
    user_id = -1
    response = client.admin.users[user_id].log_out.json.post()
    assert "success" in response.keys()
    assert response["success"] == "OK"


@pytest.mark.integration
def test_update_site_title(client):
    # Get original setting first to make operation idempotent
    settings = client.admin.site_settings.json.get()
    assert "site_settings" in settings.keys()
    title = settings["site_settings"][1]["value"]

    # Update the site setting
    data = {"title": title}
    response = client.admin.site_settings.title.put(data)
    assert response == ""


@pytest.mark.integration
def test_delete_group(client):
    # Create a new, unique group
    data = {"group": {"name": os.urandom(8).hex()}}
    response = client.admin.groups.json.post(data)
    assert "basic_group" in response.keys()
    group_id = response["basic_group"]["id"]

    # Delete the group
    response = client.admin.groups[group_id].json.delete()
    assert "success" in response.keys()
    assert response["success"] == "OK"


@pytest.mark.integration
def test_page_not_found_error(client):
    with pytest.raises(PageNotFoundError):
        response = client.nonexistant.endpoint.get()


@pytest.mark.integration
def test_unauthorized_error():
    with pytest.raises(UnauthorizedError):
        client = Discourse(BASE_URL, "graydenshand", "bad_api_key")
        client.posts.json.get()


@pytest.mark.integration
def test_rate_limit_error(client):
    with pytest.raises(RateLimitError):
        for i in range(70):
            client.categories.json.get()


@pytest.mark.integration
def test_wait_for_rate_limit():
    # Should hit rate limit, wait and ultimately retrigger the connection
    client = Discourse.from_env(raise_for_rate_limit=False)
    categories = client.categories.json.get()
    assert "category_list" in categories.keys()
