from models import Fetcher


class Act():
    def getActIndex(self, server="eu", locale="en_US"):

        self.route = '/d3/data/act'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def getAct(self, server="eu", actID=1, locale="en_US"):

        self.route = '/d3/data/act/{}'.format(actID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)