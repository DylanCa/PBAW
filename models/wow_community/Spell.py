from models import Fetcher


class Spell():
    def spell(self, server="eu", spellID=8056, locale="en_US"):

        self.route = '/wow/spell/{}'.format(spellID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)