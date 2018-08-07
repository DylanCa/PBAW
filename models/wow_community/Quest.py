import requests


class Quest():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def quest(self, server="eu", questID=13146, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/quest/{}?locale={}&apikey={}'.format(
            server, questID, locale, self.apikey)

        response = requests.get(url)

        return response.text
