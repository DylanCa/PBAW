from models import Fetcher


class Pvp():
    def leaderboards(self, server="eu", bracket="2v2", locale="en_US"):

        self.route = '/wow/leaderboard/{}'.format(bracket)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)