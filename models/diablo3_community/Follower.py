import requests


class Follower():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def getFollower(self, server="eu", followerSlug='templar', locale="en_US"):

        url = 'https://{}.api.battle.net/d3/data/follower/{}?locale={}&apikey={}'.format(
            server, followerSlug, locale, self.apikey)

        response = requests.get(url)

        return response.text
