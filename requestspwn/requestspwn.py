import pkg_resources
import os.path
import random

from requests import request as _request
from requests import head as _head
from requests import get as _get
from requests import post as _post
from requests import put as _put
from requests import patch as _patch
from requests import delete as _delete
from requests import options as _options


def load_useragents(name):
    """Use one of the default user-agent sets"""
    try:
        with open(pkg_resources.resource_filename('requestspwn', os.path.join('data', name))) as f:
            user_agents = f.read().split('\n')
        return user_agents
    except IOError:
        datasets = pkg_resources.resource_listdir('data')
        message = 'The user-agent dataset "{}" does not exist. Available datasets: {}'.format(name, datasets)
        raise FileNotFoundError(message)


def set_user_agent(user_agents, kwargs):
    """Set user agent if not already present in the headers"""
    # don't do anything if a user agent already exists
    if 'headers' in kwargs and 'User-Agent'.lower() in [header.lower() for header in kwargs['headers']]:
        return kwargs
    # load a standard dataset
    if isinstance(user_agents, str):
        user_agents = load_useragents(user_agents)
    # here we assume user_agents is an iterable of strings
    user_agent = random.choice(user_agents)
    headers = kwargs.get('headers', {})
    headers['User-Agent'] = user_agent
    kwargs['headers'] = headers
    return kwargs


def request(method, url, user_agents="latest", **kwargs):
    """Wrap the `request` method, use a random user agent.

    Additional parameters:
      user_agents -- An iterable of strings (the user agents), or a string (to load from a default dataset)
    """
    kwargs = set_user_agent(user_agents, kwargs)
    return _request(method, url, **kwargs)


def head(url, user_agents="latest", **kwargs):
    """Wrap the `head` method, use a random user agent.

    Additional parameters:
      user_agents -- An iterable of strings (the user agents), or a string (to load from a default dataset)
    """
    kwargs = set_user_agent(user_agents, kwargs)
    return _head(url, **kwargs)


def get(url, user_agents="latest", **kwargs):
    """Wrap the `get` method, use a random user agent.

    Additional parameters:
      user_agents -- An iterable of strings (the user agents), or a string (to load from a default dataset)
    """
    kwargs = set_user_agent(user_agents, kwargs)
    return _get(url, **kwargs)


def post(url, user_agents="latest", **kwargs):
    """Wrap the `post` method, use a random user agent.

    Additional parameters:
      user_agents -- An iterable of strings (the user agents), or a string (to load from a default dataset)
    """
    kwargs = set_user_agent(user_agents, kwargs)
    return _post(url, **kwargs)


def put(method, url, user_agents="latest", **kwargs):
    """Wrap the `put` method, use a random user agent.

    Additional parameters:
      user_agents -- An iterable of strings (the user agents), or a string (to load from a default dataset)
    """
    kwargs = set_user_agent(user_agents, kwargs)
    return _put(method, url, **kwargs)


def patch(url, user_agents="latest", **kwargs):
    """Wrap the `patch` method, use a random user agent.

    Additional parameters:
      user_agents -- An iterable of strings (the user agents), or a string (to load from a default dataset)
    """
    kwargs = set_user_agent(user_agents, kwargs)
    return _patch(url, **kwargs)


def delete(url, user_agents="latest", **kwargs):
    """Wrap the `delete` method, use a random user agent.

    Additional parameters:
      user_agents -- An iterable of strings (the user agents), or a string (to load from a default dataset)
    """
    kwargs = set_user_agent(user_agents, kwargs)
    return _delete(url, **kwargs)


def options(url, user_agents="latest", **kwargs):
    """Wrap the `options` method, use a random user agent.

    Additional parameters:
      user_agents -- An iterable of strings (the user agents), or a string (to load from a default dataset)
    """
    kwargs = set_user_agent(user_agents, kwargs)
    return _options(url, **kwargs)
