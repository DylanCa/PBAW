from models import Fetcher


class Follower():
    def getFollower(self, server="eu", followerSlug='templar', locale="en_US"):

        self.route = '/d3/data/follower/{}'.format(followerSlug)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)