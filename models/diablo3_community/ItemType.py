from models import Fetcher


class ItemType():
    def getItemTypeIndex(self, server="eu", locale="en_US"):

        self.route = '/d3/data/item-type'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def getItemType(self, server="eu", itemSlug='sword2h', locale="en_US"):

        self.route = '/d3/data/item-type/{}'.format(itemSlug)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
