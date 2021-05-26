import pytest
import os
from fluent_discourse import Discourse

BASE_URL = os.environ.get("DISCOURSE_URL")
USERNAME = os.environ.get("DISCOURSE_USERNAME")
API_KEY = os.environ.get("DISCOURSE_API_KEY")


@pytest.fixture
def client():
    client = Discourse(BASE_URL, USERNAME, API_KEY)
    return client
