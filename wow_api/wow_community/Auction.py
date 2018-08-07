import requests


class Auction():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def auction(self, server="eu", realm="archimonde", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/auction/data/{}?locale={}&apikey={}'.format(
            server, realm, locale, self.apikey)

        response = requests.get(url)

        return response.text
