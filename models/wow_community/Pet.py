from models import Fetcher


class Pet():
    def masterList(self, server="eu", locale="en_US"):

        self.route = '/wow/pet'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def abilities(self, server="eu", abilityID=640, locale="en_US"):

        self.route = '/wow/pet/ability/{}'.format(abilityID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def species(self, server="eu", speciesID=258, locale="en_US"):

        self.route = '/wow/pet/species/{}'.format(speciesID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def stats(self, server="eu", speciesID=258, locale="en_US"):

        self.route = '/wow/pet/stats/{}'.format(speciesID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)