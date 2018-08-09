from models import Fetcher


class Profile():
    def getRouteHero(self, account, hero):
        return '/d3/profile/{}%23{}/hero/{}'.format(
            account.split("#")[0],
            account.split("#")[1], hero)

    def getApiAccount(self,
                      server="eu",
                      account="Prototype#2971",
                      locale="en_US"):

        self.route = '/d3/profile/{}%23{}/'.format(
            account.split("#")[0],
            account.split("#")[1])

        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def getApiHero(self,
                   server="eu",
                   account="Prototype#2971",
                   hero="109407264",
                   locale="en_US"):

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.getRouteHero(account, hero))

    def getApiDetailedHeroItems(self,
                                server="eu",
                                account="Prototype#2971",
                                hero="109407264",
                                locale="en_US"):

        self.route = '{}/items'.format(self.getRouteHero(account, hero))

        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def getApiDetailedFollowerItems(self,
                                    server="eu",
                                    account="Prototype#2971",
                                    hero="109407264",
                                    locale="en_US"):

        self.route = '{}/follower-items'.format(
            self.getRouteHero(account, hero))

        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
