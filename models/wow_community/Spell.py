import requests


class Spell():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def spell(self, server="eu", spellID=8056, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/spell/{}?locale={}&apikey={}'.format(
            server, spellID, locale, self.apikey)

        response = requests.get(url)

        return response.text
