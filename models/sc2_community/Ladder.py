import requests


class Ladder():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def ladder(self, server="eu", ladderID="655", locale="en_US"):

        url = 'https://{}.api.battle.net/sc2/ladder/{}?locale={}&apikey={}'.format(
            server, ladderID, locale, self.apikey)

        response = requests.get(url)

        return response.text