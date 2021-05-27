from conf_tests import BASE_URL, client, USERNAME, API_KEY
from fluent_discourse import Discourse


def test_accumulate_strings(client):
    endpoint = client.test.a.path
    assert endpoint._cache == ["test", "a", "path"]


def test_accumulate_integers(client):
    endpoint = client.test.a.path[5]
    assert endpoint._cache == ["test", "a", "path", "5"]


def test_make_url(client):
    client._cache = ["this", "is", "a", "test", ".json"]
    assert client._make_url() == f"{BASE_URL}/this/is/a/test.json"


def test_format_base_url():
    # add trailing slash to BASE URL
    url = BASE_URL + "/"
    client = Discourse(url, USERNAME, API_KEY)
    assert client._base_url == BASE_URL
