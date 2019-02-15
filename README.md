# requestspwn
Drop-in replacement for the `requests` library with random user agents as default. Designed for Attack/Defense CTF competitions.

## Installation
```
$ pip install requestspwn
```

## Usage
Just replace the import lines like this:

* `import requests` to `import requestspwn as requests`
* `from requests` to `from requestspwn`

Example:

```python
from requestspwn import get
r = get('https://www.example.com')
```

Additionally, you can provide a list of user agents to choose from:

```python
from requestspwn import get
user_agents = [
	"Mozilla/5.0 (Windows NT 6.3; WOW64;Trident/7.0; rv:11.0) like Gecko",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0"
]
r = get('https://www.example.com', user_agents=user_agents)
```

You can also use one of the datasets provided by default:

```python
from requestspwn import get
r = get('https://www.example.com', user_agents='ructfe2017')
```

## Additional notes
`requestspwn` will use a random user agent as default. If you pass a custom User-Agent header in the `headers` parameter, `requestspwn` will NOT replace it.

`requestspwn` wraps the `request`, `head`, `get`, `post`, `put`, `patch`, `delete`, `options` functions, and nothing else.