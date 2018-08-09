from models import Fetcher


class DataRessources():
    def battlegroups(self, server="eu", locale="en_US"):

        self.route = '/wow/data/battlegroups'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def characterRaces(self, server="eu", locale="en_US"):

        self.route = '/wow/data/character/races'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def characterClasses(self, server="eu", locale="en_US"):

        self.route = '/wow/data/character/classes'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def characterAchievements(self, server="eu", locale="en_US"):

        self.route = '/wow/data/character/achievements'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def guildRewards(self, server="eu", locale="en_US"):

        self.route = '/wow/data/guild/rewards'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def guildPerks(self, server="eu", locale="en_US"):

        self.route = '/wow/data/guild/perks'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def guildAchievements(self, server="eu", locale="en_US"):

        self.route = '/wow/data/guild/achievements'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def itemClasses(self, server="eu", locale="en_US"):

        self.route = '/wow/data/item/classes'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def talents(self, server="eu", locale="en_US"):

        self.route = '/wow/data/talents'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def petTypes(self, server="eu", locale="en_US"):

        self.route = '/wow/data/pet/types'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
