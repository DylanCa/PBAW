import requests


class Boss():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def masterList(self, server="eu", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/boss/?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def boss(self, server="eu", bossID="24723", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/boss/{}?locale={}&apikey={}'.format(
            server, bossID, locale, self.apikey)

        response = requests.get(url)

        return response.text
