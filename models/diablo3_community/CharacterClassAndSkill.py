import requests


class CharacterClassAndSkill():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def getCharacterClass(self,
                          server="eu",
                          classSlug='barbarian',
                          locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/hero/{}?locale={}&apikey={}'.format(
            server, classSlug, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def getApiSkill(self,
                    server="eu",
                    classSlug='barbarian',
                    skillSlug='bash',
                    locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/hero/{}/skill/{}?locale={}&apikey={}'.format(
            server, classSlug, skillSlug, locale, self.apikey)

        response = requests.get(url)

        return response.text
