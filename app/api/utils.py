import requests


def post_basic_auth(*args, **kwargs):
    user = kwargs.get('user')
    key = kwargs.get('key')
    payload = kwargs.get('payload')
    endpoint = kwargs.get('endpoint')
    return requests.post(endpoint, auth=(user, key), data=payload)


def post_bearer_auth(*args, **kwargs):
    key = kwargs.get('key')
    endpoint = kwargs.get('endpoint')
    payload = kwargs.get('payload')
    headers = {
        'Authorization': f'Bearer {key}',
    }
    return requests.post(endpoint, headers=headers, json=payload)
