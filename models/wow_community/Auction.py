from models import Fetcher


class Auction():
    def auction(self, server="eu", realm="archimonde", locale="en_US"):

        self.route = '/wow/auction/data/{}'.format(realm)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
