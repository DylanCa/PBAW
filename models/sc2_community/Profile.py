from models import Fetcher


class Profile():
    def getRoute(self, accID, region, name):
        return 'sc2/profile/{}/{}/{}/'.format(accID, region, name)

    def profile(self,
                server="eu",
                accID=20443743,
                region=1,
                name="Prototype",
                locale="en_US"):

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.getRoute(accID, region, name))

    def ladders(self,
                server="eu",
                accID=20443743,
                region=1,
                name="Prototype",
                locale="en_US"):

        self.route = self.getRoute(accID, region, name) + 'ladders'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def matchHistory(self,
                     server="eu",
                     accID=20443743,
                     region=1,
                     name="Prototype",
                     locale="en_US"):

        self.route = self.getRoute(accID, region, name) + 'matches'
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
