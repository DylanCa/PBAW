from models import Fetcher


class Zone():
    def masterList(self, server="eu", locale="en_US"):

        self.route = '/wow/zone'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def zone(self, server="eu", zoneID=4131, locale="en_US"):

        self.route = '/wow/zone/{}'.format(zoneID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)