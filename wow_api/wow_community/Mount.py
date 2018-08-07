import requests


class Mount():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def masterList(self, server="eu", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/mount/?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text
