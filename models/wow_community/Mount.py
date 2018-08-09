from models import Fetcher


class Mount():
    def masterList(self, server="eu", locale="en_US"):

        self.route = '/wow/mount/'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)