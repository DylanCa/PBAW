import requests


class ArtisanAndRecipe():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def getArtisan(self, server="eu", artisanSlug='blacksmith',
                   locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/artisan/{}?locale={}&apikey={}'.format(
            server, artisanSlug, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def getRecipe(self,
                  server="eu",
                  artisanSlug='blacksmith',
                  recipeSlug='apprentice-flamberge',
                  locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/artisan/{}/recipe/{}?locale={}&apikey={}'.format(
            server, artisanSlug, recipeSlug, locale, self.apikey)

        response = requests.get(url)

        return response.text
