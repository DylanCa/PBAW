import requests


class Pet():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def masterList(self, server="eu", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/pet/?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def abilities(self, server="eu", abilityID=640, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/pet/ability/{}?locale={}&apikey={}'.format(
            server, abilityID, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def species(self, server="eu", speciesID=258, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/pet/species/{}?locale={}&apikey={}'.format(
            server, speciesID, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def stats(self, server="eu", speciesID=258, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/pet/stats/{}?locale={}&apikey={}'.format(
            server, speciesID, locale, self.apikey)

        response = requests.get(url)

        return response.text