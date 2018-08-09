from models import Fetcher


class Achievement():
    
    def achievement(self, server="eu", achievementID="2144", locale="en_US"):

        self.route = '/wow/achievement/{}'.format(achievementID)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
