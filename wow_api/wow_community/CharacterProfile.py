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

    def achievements(self,
                     server="eu",
                     realm="archimonde",
                     characterName="Protòtype",
                     locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=achievements&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def appearance(self,
                   server="eu",
                   realm="archimonde",
                   characterName="Protòtype",
                   locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=appearance&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def feed(self,
             server="eu",
             realm="archimonde",
             characterName="Protòtype",
             locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=feed&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def guild(self,
              server="eu",
              realm="archimonde",
              characterName="Protòtype",
              locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=guild&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def hunterPets(self,
                   server="eu",
                   realm="archimonde",
                   characterName="Protòtype",
                   locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=hunterPets&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def items(self,
              server="eu",
              realm="archimonde",
              characterName="Protòtype",
              locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=items&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def mounts(self,
               server="eu",
               realm="archimonde",
               characterName="Protòtype",
               locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=mounts&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def pets(self,
             server="eu",
             realm="archimonde",
             characterName="Protòtype",
             locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=pets&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def petSlots(self,
                 server="eu",
                 realm="archimonde",
                 characterName="Protòtype",
                 locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=petSlots&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def professions(self,
                    server="eu",
                    realm="archimonde",
                    characterName="Protòtype",
                    locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=professions&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def progression(self,
                    server="eu",
                    realm="archimonde",
                    characterName="Protòtype",
                    locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=progression&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def pvp(self,
            server="eu",
            realm="archimonde",
            characterName="Protòtype",
            locale="en_US"):

        url = 'https://{}.api.battle.net/wow/character/{}/{}?fields=pvp&locale={}&apikey={}'.format(
            server, realm, characterName, locale, self.apikey)

        response = requests.get(url)

        return response.text
