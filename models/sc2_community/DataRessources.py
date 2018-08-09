from models import Fetcher


class DataRessources():
    def achievements(self, server="eu", locale="en_US"):

        self.route = '/sc2/data/achievements'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def rewards(self, server="eu", locale="en_US"):

        self.route = '/sc2/data/rewards'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)