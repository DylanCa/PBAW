import requests


class Item():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def getItem(self,
                server="eu",
                itemSlugAndID='corrupted-ashbringer-Unique_Sword_2H_104_x1',
                locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/item/{}?locale={}&apikey={}'.format(
            server, itemSlugAndID, locale, self.apikey)

        response = requests.get(url)

        return response.text
