from models import Fetcher


class CharacterClassAndSkill():
    def getCharacterClass(self,
                          server="eu",
                          classSlug='barbarian',
                          locale="en_US"):

        self.route = '/d3/data/hero/{}'.format(classSlug)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def getApiSkill(self,
                    server="eu",
                    classSlug='barbarian',
                    skillSlug='bash',
                    locale="en_US"):

        self.route = '/d3/data/hero/{}/skill/{}'.format(classSlug, skillSlug)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)
