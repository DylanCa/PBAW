import requests


class DataRessources():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def achievements(self, server="eu", name="Prototype", locale="en_US"):

        url = 'https://{}.api.battle.net/sc2/data/achievements?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def achievements(self, server="eu", name="Prototype", locale="en_US"):

        url = 'https://{}.api.battle.net/sc2/data/rewards?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text