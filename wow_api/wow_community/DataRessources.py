import requests


class DataRessources():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def battlegroups(self, server="eu", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/battlegroups/?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def characterRaces(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/character/races?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def characterClasses(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/character/classes?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def characterAchievements(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/character/achievements?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def guildRewards(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/guild/rewards?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def guildPerks(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/guild/perks?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def guildAchievements(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/guild/achievements?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def itemClasses(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/item/classes?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def talents(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/talents?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def petTypes(self, server="eu", zoneID=4131, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/data/pet/types?locale={}&apikey={}'.format(
            server, locale, self.apikey)

        response = requests.get(url)

        return response.text
