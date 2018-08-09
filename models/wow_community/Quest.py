from models import Fetcher


class Quest():
    def quest(self, server="eu", questID=13146, locale="en_US"):

        self.route = '/wow/quest/{}'.format(questID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)