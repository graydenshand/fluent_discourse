import requests
from json.decoder import JSONDecodeError


class Discourse:
    def __init__(self, base_url, username, api_key, cache=None):
        if base_url[-1] == "/":
            # Remove trailing slash from base_url
            base_url = base_url[:-1]
        self._base_url = base_url
        self._username = username
        self._api_key = api_key
        self._cache = cache or []
        self._headers = {
            "Content-Type": "application/json",
            "Api-Username": self._username,
            "Api-Key": self._api_key,
        }

    def _(self, name):
        # Add name to cache, return self
        self._cache += [str(name)]
        return self

    def request(self, method, data=None, params=None):
        # Make a request
        url = self._make_url()

        r = requests.request(
            method, url, json=data, params=params, headers=self._headers
        )

        # Clear cache
        self._cache = []

        if r.status_code == 200:
            try:
                return r.json()
            except JSONDecodeError as e:
                # Request succeeded but response body was not valid JSON
                return r.text
        else:
            r.raise_for_status()

    def get(self, data=None):
        # Make a get request
        return self.request("GET", params=data)

    def post(self, data=None):
        # Make a post request
        return self.request("POST", data=data)

    def put(self, data=None):
        # Make a put request
        return self.request("PUT", data=data)

    def delete(self, data=None):
        # Make a delete request
        return self.request("DELETE", data=data)

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
