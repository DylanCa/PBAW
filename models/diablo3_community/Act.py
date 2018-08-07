import requests


class Act():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def getActIndex(self, server="eu", locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/act?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def getAct(self, server="eu", actID=1, locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/act/{}?locale={}&apikey={}'.format(
            server, actID, locale, self.apikey)

        response = requests.get(url)

        return response.text
