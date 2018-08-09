from models import Fetcher


class Ladder():
    def ladder(self, server="eu", ladderID="655", locale="en_US"):

        self.route = '/sc2/ladder/{}'.format(ladderID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)