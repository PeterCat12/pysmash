from pysmash import exceptions
import requests


SMASHGG_API_URL = 'api.smash.gg'


def get(uri, params=[]):
    """"Performs a get request and return the contents of the response"""
    params = _prepare_params(params)
    url = "https://%s/%s" % (SMASHGG_API_URL, uri + params)

    r = requests.get(url)

    data = r.json()
    if r.status_code == 200:
        return data
    raise exceptions.ResponseError(data['message'], r.status_code)


def _prepare_params(params):
    """return params as SmashGG friendly query string"""
    query_string = ''

    if len(params) == 0:
        return query_string

    prefix = '?expand[]='
    query_string = prefix + '&expand[]='.join(params)

    return query_string
