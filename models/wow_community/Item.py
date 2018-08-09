from models import Fetcher


class Item():

    def item(self, server="eu", itemID=18803, locale="en_US"):

        self.route = '/wow/item/{}'.format(itemID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def itemSet(self, server="eu", setID=1060, locale="en_US"):

        self.route = '/wow/item/set/{}'.format(setID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)