# Fluent Discourse
<p>
	<a href="https://github.com/graydenshand/fluent_discourse/actions/workflows/build.yml"><img src="https://github.com/graydenshand/fluent_discourse/actions/workflows/build.yml/badge.svg?branch=main" alt="Build and test"/></a>
	<a href="https://codecov.io/gh/graydenshand/fluent_discourse"><img src="https://codecov.io/gh/graydenshand/fluent_discourse/branch/main/graph/badge.svg?token=Z9RR4GWFXI" alt="Code Coverage" /></a>
</p>

This package implements a [fluent interface](https://en.wikipedia.org/wiki/Fluent_interface) to the Discourse API. 

What does that mean?

Instead of mapping every endpoint and method to a unique function, we present a framework for making any request.

This means, with very little code, **this package is fully compatible with the Discourse API, including undocumented endpoints, endpoints from plugins, and endpoints that have yet to be created.** 

## Installation
The easiest way to install is via PyPI
```bash
pip install fluent-discourse
```

## Usage
### Setting up a client
Set up a client by specifying a base_url, username, and api_key for it to use. 

```python
from fluent_discourse import Discourse

client = Discourse(base_url="http://localhost:3000", username="test_user", api_key="a0a2d176b3cfbadd36ac2f46ccbd701bf45dfd6f47836e99d570bf7e0ae04af8", raise_for_rate_limit=True)
```

Or, you can set three environment variables:
```language
export DISCOURSE_URL=http://localhost:3000
export DISCOURSE_USERNAME=test_user
export DISCOURSE_API_KEY=a0a2d176b3cfbadd36ac2f46ccbd701bf45dfd6f47836e99d570bf7e0ae04af8
```
Then you can use the `from_env()` class method to instantiate the client:
```python
from fluent_discourse import Discourse
client = Discourse.from_env(raise_for_rate_limit=False)
```

In either case, the `raise_for_rate_limit` parameter is optional (defaults to True) and controls how the client will respond to RateLimitErrors. If `True`, the client will raise a `RateLimitError`; if `False`, it will wait the suggested time for the RateLimit counter to reset and retry the request.

Once your client is initialized, you can can begin making requests. Let's first take an example to see how this works.

### Basic Example
Let's say we want to get the latest posts, [here's the appropriate endpoint](https://docs.discourse.org/#tag/Posts/paths/~1posts.json/get). We need to make a `GET` request to `/posts.json`. Here's how you do it with the client we've set up. 

```python
latest = client.posts.json.get()
```

I hope that gives you an idea of how this works. Instead of calling a specific function that is mapped to this endpoint/method combination, we construct the request dynamically using a form of method chaining. Finally, we use the special methods `get()`, `put()`, `post()`, or `delete()` to trigger a request to the specified endpoint. 


### Passing IDs and Python Reserved Words
Let's look at another example. This time we want to add users to a group, [here's the endpoint we want to hit](https://docs.discourse.org/#tag/Groups/paths/~1groups~1{id}~1members.json/put). Specifically, we want to add users to the group with `id=5`, so we need to send a `PUT` request to `/groups/5/members.json`.

Here's how to do that with this package:
```python
data = {
	"usernames": "username1,username2"
}
client.groups[5].members.json.put(data)
```
Notice that we use a slightly different syntax ("indexed at" brackets) to pass in numbers. This is because of the naming constraints of python attributes. We also run into problems with reserved words like `for` and `is`. 

If you ever need to construct a URL that contains numbers or reserved words, there are two methods. 

```python
# These throw Syntax errors
## Numbers are not allowed
client.groups.5.members.json.put(data)
## "is" and "for" are reserved words
client.is.this.for.me.get()

# Valid approaches
## Using brackets
client.groups[5].members.json.put(data)
## Using the _() method
client._("is").this._("for").me.get()
```

As you can see, you can either use brackets `[]` or the underscore method `_()` to handle integers or reserved words.

### Passing data
The `get()`, `put()`, `post()`, and `delete()` methods each take a single optional argument, `data`, which is a dictionary of data to pass along with the request.

For the `put()`, `post()`, and `delete()` methods the data is sent in the body of the request (as JSON).

For the `get()` method the data is added to the url as query parameters. 

### Exceptions
There are a few custom exceptions defined in this class. 

`DiscourseError`
* A catch all, and parent class for errors resulting from this package. Raised when Discourse responds with an error that doesn't fall into the other, more specific, categories (e.g. a 500 error). 

`UnauthorizedError`
* Raised when Discourse responds with a 403 error, and indicates that invalid credentials were used to set up the client. 

`RateLimitError`
* Triggered when Discourse responds with a 429 response and the client is configured with `raise_for_rate_limit=True`.

`PageNotFoundError`
* Raised when Discourse responds with a 404, indicating either that the page does not exist or the current user does not have access to that page. 

You can import any of these errors directly from the package. 
```python
from fluent_discourse import DiscourseError
```

## Contributing
Thanks for your interest in contributing to this project! For bug tracking and other issues please use the issue tracker on GitHub. 

### Testing
This package strives for 100% test coverage. Tests are run through tox. They are split into unit and integration tests. Unit tests are self contained, integration tests send requests to a server. 

Although all integration tests have been tested against a live Discourse server, we set up a mock-server for CI testing. 

Three environment variables are required to set up the test client:
* `DISCOURSE_URL`: The base url of the discourse (e.g. `http://localhost:4200`)
* `DISCOURSE_USERNAME`: The username of the user to interact as, importantly the tests require that this user has admin privileges. 
* `DISCOURSE_API_KEY`: An API key configured to work with the specified user. This key should have global scopes.

To run **all** tests (against a live discourse):
```bash
tox
```

To run just **unit** tests:
```bash
tox -- -m "not integration"
```

To run just **integration** tests (against a live discourse):
```bash
tox -- -m "integration"
```

To set up the mock server and run the tests against that, set your `DISCOURSE_URL` env variable to `http://127.0.0.1:5000` and run:
```bash
./run_tests_w_mock_server.sh
```

100% test coverage is important. If you make changes, please ensure those changes are reflected in the tests as well. Particularly for integration tests, run them both against a live discourse server and the mock server. Please extend and adjust the mock server as necessary to reproduce the test results on a live server accurately. 

### Style Linting
Please use [black](https://github.com/psf/black) to reformat any code changes before committing those changes. 

Just run:
```bash
black .
```

## Acknowledgements
I stole the idea for a fluent API interface (and some code as a starting point) from SendGrid's Python API. [Here's a resouce that explains their approach](https://sendgrid.com/blog/using-python-to-implement-a-fluent-interface-to-any-rest-api/).

There's a [Universal Client](https://universal-client.readthedocs.io/en/latest/) library that implements this framework as a flexible interface to ANY api. In contrast, this package is tailored specifically to Discourse's API including better error handling. 