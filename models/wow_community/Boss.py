from models import Fetcher


class Boss():

    def masterList(self, server="eu", locale="en_US"):

        return Fetcher.fetchData(
            server=server, locale=locale, route='/wow/boss/')

    def boss(self, server="eu", bossID="24723", locale="en_US"):

        self.route = '/wow/boss/{}'.format(bossID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
