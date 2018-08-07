import requests


class Achievement():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def achievement(self, server="eu", achievementID="2144", locale="en_US"):

        url = 'https://{}.api.battle.net/wow/achievement/{}?locale={}&apikey={}'.format(
            server, achievementID, locale, self.apikey)

        response = requests.get(url)

        return response.text
