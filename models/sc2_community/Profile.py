import requests


class Profile():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def profile(self,
                server="eu",
                accID=20443743,
                region=1,
                name="Prototype",
                locale="en_US"):

        url = 'https://{}.api.battle.net/sc2/profile/{}/{}/{}/?locale={}&apikey={}'.format(
            server, accID, region, name, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def ladders(self,
                server="eu",
                accID=20443743,
                region=1,
                name="Prototype",
                locale="en_US"):

        url = 'https://{}.api.battle.net/sc2/profile/{}/{}/{}/ladders?locale={}&apikey={}'.format(
            server, accID, region, name, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def matchHistory(self,
                     server="eu",
                     accID=20443743,
                     region=1,
                     name="Prototype",
                     locale="en_US"):

        url = 'https://{}.api.battle.net/sc2/profile/{}/{}/{}/matches?locale={}&apikey={}'.format(
            server, accID, region, name, locale, self.apikey)

        response = requests.get(url)

        return response.text
