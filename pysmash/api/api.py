from pysmash.core import exceptions
import requests
from urllib.parse import urlencode


SMASHGG_API_URL = 'api.smash.gg'


def get(uri, params=None):
    if params is None:
        params = {}

    """"Performs a get request and return the contents of the response"""
    url = "https://%s/%s" % (SMASHGG_API_URL, uri + '?' + urlencode(params, True))

    r = requests.get(url)

    data = r.json()
    if r.status_code == 200:
        return data
    raise exceptions.ResponseError(data['message'], r.status_code)
