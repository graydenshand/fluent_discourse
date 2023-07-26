import requests
from json.decoder import JSONDecodeError
from .errors import *
import time
import logging
import os
from copy import deepcopy

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Discourse:
    def __init__(
        self, base_url, username, api_key, cache=None, raise_for_rate_limit=True
    ):
        if base_url[-1] == "/":
            # Remove trailing slash from base_url
            base_url = base_url[:-1]
        self._base_url = base_url
        self._username = username
        self._api_key = api_key
        self._cache = cache or []
        self._raise_for_rate_limit = raise_for_rate_limit
        self._headers = {
            "Content-Type": "application/json",
            "Api-Username": self._username,
            "Api-Key": self._api_key,
        }

    @staticmethod
    def from_env(raise_for_rate_limit=True):
        base_url = os.environ.get("DISCOURSE_URL")
        username = os.environ.get("DISCOURSE_USERNAME")
        api_key = os.environ.get("DISCOURSE_API_KEY")
        return Discourse(
            base_url, username, api_key, raise_for_rate_limit=raise_for_rate_limit
        )

    def _(self, name):
        # Add name to cache, return self
        return Discourse(
            self._base_url,
            self._username,
            self._api_key,
            self._cache + [str(name)],
            self._raise_for_rate_limit,
        )

    def _request(self, method, url, data=None, params=None):
        r = requests.request(
            method, url, json=data, params=params, headers=self._headers
        )

        if r.status_code == 200:
            try:
                return r.json()
            except JSONDecodeError as e:
                # Request succeeded but response body was not valid JSON
                return r.text
        else:
            return self._handle_error(r, method, url, data, params)

    def _handle_error(self, response, method, url, data, params):
        if response.status_code == 404:
            raise PageNotFoundError(
                f"The requested page was not found, or you do not have permission to access it: {response.url}"
            )
        elif response.status_code == 403:
            raise UnauthorizedError("Invalid credentials")
        elif response.status_code == 429:
            if self._raise_for_rate_limit:
                raise RateLimitError("Rate limit hit")
            else:
                self._wait_for_rate_limit(response, method, url, data, params)
                return self._request(method, url, data, params)
        else:
            raise DiscourseError(
                f"Unhandled discourse exception: {response.status_code} - {response.text}"
            )

    def _wait_for_rate_limit(self, response, method, url, data, params):
        # get the number of seconds to wait before retrying, add 1 for 0 errors
        wait_seconds = int(response.json()["extras"]["wait_seconds"]) + 1
        # add piece to rate limit and then try again
        logger.warning(
            f"Discourse rate limit hit, trying again in {wait_seconds} seconds"
        )
        # sleep for wait_seconds
        time.sleep(wait_seconds)
        return

    def get(self, data=None):
        # Make a get request
        url = self._make_url()
        return self._request("GET", url, params=data)

    def post(self, data=None):
        # Make a post request
        url = self._make_url()
        return self._request("POST", url, data=data)

    def put(self, data=None):
        # Make a put request
        url = self._make_url()
        return self._request("PUT", url, data=data)

    def delete(self, data=None):
        # Make a delete request
        url = self._make_url()
        return self._request("DELETE", url, data=data)

    def _make_url(self):
        # Build the request url from cache segments
        endpoint = "/".join(self._cache)
        # strip forward slash from e.g. '.json' or '.rss' segments if passed
        endpoint = endpoint.replace("/.", ".")

        url = f"{self._base_url}/{endpoint}"
        return url

    def __getattr__(self, name):
        """
        Calling self.attribute_name adds "attribute_name" to self._cache

        Only works for strings
        """
        if name == "json":
            return self._(f".{name}")
        return self._(name)

    def __getitem__(self, name):
        """
        Calling self[attribute_name] adds "attribute_name" to self._cache

        Primarily for integers
        """
        return self._(name)
