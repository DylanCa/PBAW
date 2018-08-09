from models import Fetcher


class RealmStatus():
    def realmStatus(self, server="eu", locale="en_US"):

        self.route = '/wow/realm/status'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)