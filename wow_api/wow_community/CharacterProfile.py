import requests


class CharacterProfile():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def characterProfile(self,
                         server="eu",
                         realm="archimonde",
                         characterName="Protòtype",
                         locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text
