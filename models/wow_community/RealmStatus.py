import requests


class RealmStatus():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def realmStatus(self, server="eu", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/realm/status?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text
