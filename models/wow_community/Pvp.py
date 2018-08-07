import requests


class Pvp():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def leaderboards(self, server="eu", bracket="2v2", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/leaderboard/{}?locale={}&apikey={}'.format(
            server, bracket, locale, self.apikey)

        response = requests.get(url)

        return response.text
