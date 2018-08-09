from models.local_config import API_KEY
import requests


def fetchData(server='eu', route='', params='', locale='en_US'):

    if params != '':
        params = params + '&'

    return requests.get(
        'https://{}.api.battle.net/{}?{}locale=en_US&apikey={}'.format(
            server, route, params, API_KEY)).text
