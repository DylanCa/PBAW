from models import Fetcher


class ChallengeMode():
    def realmLeaderboard(self, server="eu", realm="archimonde",
                         locale="en_US"):

        self.route = '/wow/challenge/{}'.format(realm)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def regionLeaderboard(self, server="eu", locale="en_US"):

        return Fetcher.fetchData(
            server=server, locale=locale, route='/wow/challenge/region')
