from models import Fetcher


class ArtisanAndRecipe():
    def getArtisan(self, server="eu", artisanSlug='blacksmith',
                   locale="en_US"):

        self.route = '/d3/data/artisan/{}'.format(artisanSlug)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def getRecipe(self,
                  server="eu",
                  artisanSlug='blacksmith',
                  recipeSlug='apprentice-flamberge',
                  locale="en_US"):

        self.route = '/d3/data/artisan/{}/recipe/{}'.format(
            artisanSlug, recipeSlug)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
