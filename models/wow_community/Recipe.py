import requests


class Recipe():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def recipe(self, server="eu", recipeID=33994, locale="en_US"):

        url = 'https://{}.api.battle.net/wow/recipe/{}?locale={}&apikey={}'.format(
            server, recipeID, locale, self.apikey)

        response = requests.get(url)

        return response.text
