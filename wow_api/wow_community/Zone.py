import requests


class Zone():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def masterList(self, server="eu", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/zone/?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def zone(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/zone/{}?locale={}&apikey={}'.format(
            server, zoneID, locale, self.apikey)

        response = requests.get(url)

        return response.text
