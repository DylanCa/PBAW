import requests


class Item():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def item(self, server="eu", itemID=18803, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/item/{}?locale={}&apikey={}'.format(
            server, itemID, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def itemSet(self, server="eu", setID=1060, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/item/set/{}?locale={}&apikey={}'.format(
            server, setID, locale, self.apikey)

        response = requests.get(url)

        return response.text