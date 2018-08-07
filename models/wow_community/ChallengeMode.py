import requests


class ChallengeMode():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def realmLeaderboard(self, server="eu", realm="archimonde",
                         locale="en_US"):

        url = 'https://{}.api.battle.net/wow/challenge/{}?locale={}&apikey={}'.format(
            server, realm, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def regionLeaderboard(self, server="eu", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/challenge/region?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text