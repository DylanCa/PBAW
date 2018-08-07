import requests


class GuildProfile():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def guildProfile(self,
                     server="eu",
                     realm="archimonde",
                     guild="Jardiland",
                     locale="en_US",
                     fields="achievements,challenge"):

        url = 'https://{}.api.battle.net/wow/guild/{}/{}?fields={}&locale={}&apikey={}'.format(
            server, realm, guild, fields, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def members(self,
                server="eu",
                realm="archimonde",
                guild="Jardiland",
                locale="en_US"):

        url = 'https://{}.api.battle.net/wow/guild/{}/{}?fields=members&locale={}&apikey={}'.format(
            server, realm, guild, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def achievements(self,
                     server="eu",
                     realm="archimonde",
                     guild="Jardiland",
                     locale="en_US"):

        url = 'https://{}.api.battle.net/wow/guild/{}/{}?fields=achievements&locale={}&apikey={}'.format(
            server, realm, guild, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def news(self,
             server="eu",
             realm="archimonde",
             guild="Jardiland",
             locale="en_US"):

        url = 'https://{}.api.battle.net/wow/guild/{}/{}?fields=news&locale={}&apikey={}'.format(
            server, realm, guild, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def challenge(self,
                  server="eu",
                  realm="archimonde",
                  guild="Jardiland",
                  locale="en_US"):

        url = 'https://{}.api.battle.net/wow/guild/{}/{}?fields=challenge&locale={}&apikey={}'.format(
            server, realm, guild, locale, self.apikey)

        response = requests.get(url)

        return response.text
