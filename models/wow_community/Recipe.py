from models import Fetcher


class Recipe():
    def recipe(self, server="eu", recipeID=33994, locale="en_US"):

        self.route = '/wow/recipe/{}'.format(recipeID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)