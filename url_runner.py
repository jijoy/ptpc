import requests
import json

from config import DEBUG


def get(url, query_data=None, headers=None, return_json=False):
    res = requests.get(url, params=query_data, headers=headers)
    if DEBUG:
        print res.status_code
    if return_json is True:
        return res.json()
    else:
        return res.text

def post(url, data=None, headers=None, return_json=False):
    res = requests.post(url, data=json.dumps(data), headers=headers)
    if return_json is True:
        return res.json()
    else:
        return res.text

def put(url, data=None, headers=None, return_json=False):
    res = requests.put(url, data=json.dumps(data), headers=headers)
    if return_json is True:
        return res.json()
    else:
        return res.text

def delete(url, data=None, headers=None, return_json=False):
    res = requests.delete(url, data=json.dumps(data), headers=headers)
    if return_json is True:
        return res.json()
    else:
        return res.text