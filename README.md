# Fluent Discourse
<p>
	<a href="https://github.com/graydenshand/fluent_discourse/actions/workflows/build.yml"><img src="https://github.com/graydenshand/fluent_discourse/actions/workflows/build.yml/badge.svg?branch=main" alt="Build and test"/></a>
	<a href="https://codecov.io/gh/graydenshand/fluent_discourse"><img src="https://codecov.io/gh/graydenshand/fluent_discourse/branch/main/graph/badge.svg?token=Z9RR4GWFXI" alt="Code Coverage" /></a>
</p>

This package implements a fluent interface to the Discourse API. 

Instead of mapping every endpoint and method to a unique function, we present a framework for making any request.

This means, with very little code, this package is fully compatible with the Discourse API. This includes undocumented endpoints as well as endpoints that have yet to be created. 

## Installation
The easiest way to install is via PyPI
```bash
pip install fluent-discourse
```


## Usage
Set up a client by specifying a base_url, username, and api_key for it to use. 

```python
from fluent_discourse import Discourse

client = Discourse(base_url="http://localhost:3000", username="test_user", api_key="a0a2d176b3cfbadd36ac2f46ccbd701bf45dfd6f47836e99d570bf7e0ae04af8")
```

Once your client is initialized, you can can begin making requests. Let's take an example to see how this works.

Let's say we want to get the latest posts, [here's the appropriate endpoint](https://docs.discourse.org/#tag/Posts/paths/~1posts.json/get). We need to make a `GET` request to `/posts.json`. Here's how you do it with the client we've set up. 

```python
latest = client.posts.json.get()
```

I hope that gives you an idea of how this works. Instead of calling a specific function that is mapped to this endpoint/method combination, we construct the request dynamically using a form of method chaining.

Let's look at another example. This time we want to add users to a group, [here's the endpoint we want to hit](https://docs.discourse.org/#tag/Groups/paths/~1groups~1{id}~1members.json/put). Specifically, we want to add users to the group with `id=5`, so we need to send a `PUT` request to `/groups/5/members.json`.

Here's how to do that with this package:
```python
data = {
	"usernames": "username1,username2"
}
client.groups[5].members.json.put(data=data)
```

A few things to note here:
* We can inject numbers into the endpoint using the "index at" bracket syntax `...groups[5]...`.
* Data for the request is passed as a dictionary to the `data` parameter. 


## Contributing
Thanks for your interest in contributing to this project! For bug tracking and other issues please use the issue tracker on GitHub. 

### Testing
Tests are run through tox. They are split into unit and integration tests. The integration tests require a live discourse. As such all tests should strive to be idempotent; however, despite striving to be idempotent it's still recommended to set up a local install of Discourse to run the tests against. All that's needed is a single admin user and an api key.

Three environment variables are required to set up the test client:
* `DISCOURSE_URL`: The base url of the discourse (e.g. `http://localhost:4200`)
* `DISCOURSE_USERNAME`: The username of the user to interact as, importantly the tests require that this user has admin privileges. 
* `DISCOURSE_API_KEY`: An API key configured to work with the specified user. This key should have global scopes.

To run **all** tests:
```bash
tox
```

To run just **unit** tests:
```bash
tox -- -m "not integration"
```

To run just **integration** tests:
```bash
tox -- -m "integration"
```

### Style Linting
Please use [black](https://github.com/psf/black) to reformat any code changes before committing those changes. 

Just run:
```bash
black .
```


## Acknowledgements
I stole the idea for a fluent API interface (and some code as a starting point) from SendGrid's Python API. [Here's a resouce that explains their approach](https://sendgrid.com/blog/using-python-to-implement-a-fluent-interface-to-any-rest-api/).

There's a [Universal Client](https://universal-client.readthedocs.io/en/latest/) library that implements this framework as a flexible interface to ANY api. In contrast, this package is tailored specifically to Discourse's API including better error handling. 