from models import Fetcher


class GuildProfile():
    def __init__(self):
        self.route = '/wow/guild/{}/{}'

    def guildProfile(self,
                     server="eu",
                     realm="archimonde",
                     guildName="Jardiland",
                     locale="en_US",
                     fields="achievements,challenge"):

        self.route = self.route.format(realm, guildName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=achievements,challenge')

    def members(self,
                server="eu",
                realm="archimonde",
                guildName="Jardiland",
                locale="en_US"):

        self.route = self.route.format(realm, guildName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=members')

    def achievements(self,
                     server="eu",
                     realm="archimonde",
                     guildName="Jardiland",
                     locale="en_US"):

        self.route = self.route.format(realm, guildName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=achievements')

    def news(self,
             server="eu",
             realm="archimonde",
             guildName="Jardiland",
             locale="en_US"):

        self.route = self.route.format(realm, guildName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=news')

    def challenge(self,
                  server="eu",
                  realm="archimonde",
                  guildName="Jardiland",
                  locale="en_US"):

        self.route = self.route.format(realm, guildName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=challenge')
