from models import Fetcher


class Item():
    def getItem(self,
                server="eu",
                itemSlugAndID='corrupted-ashbringer-Unique_Sword_2H_104_x1',
                locale="en_US"):

        self.route = '/d3/data/item/{}'.format(itemSlugAndID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
