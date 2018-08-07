import requests


class ItemType():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def getItemTypeIndex(self, server="eu", locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/item-type?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def getItemType(self, server="eu", itemSlug='sword2h', locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/item-type/{}?locale={}&apikey={}'.format(
            server, itemSlug, locale, self.apikey)

        response = requests.get(url)

        return response.text
