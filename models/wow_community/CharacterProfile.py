from models import Fetcher


class CharacterProfile():
    def __init__(self):
        self.route = '/wow/character/{}/{}'

    def characterProfile(self,
                         server="eu",
                         realm="archimonde",
                         characterName="Protòtype",
                         locale="en_US"):

        self.route = self.route.format(realm, characterName)
        return Fetcher.fetchData(
            server=server, locale=locale, route=self.route)

    def achievements(self,
                     server="eu",
                     realm="archimonde",
                     characterName="Protòtype",
                     locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=achievements')

    def appearance(self,
                   server="eu",
                   realm="archimonde",
                   characterName="Protòtype",
                   locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=appearance')

    def feed(self,
             server="eu",
             realm="archimonde",
             characterName="Protòtype",
             locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=feed')

    def guild(self,
              server="eu",
              realm="archimonde",
              characterName="Protòtype",
              locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=guild')

    def hunterPets(self,
                   server="eu",
                   realm="archimonde",
                   characterName="Protòtype",
                   locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=hunterPets')

    def items(self,
              server="eu",
              realm="archimonde",
              characterName="Protòtype",
              locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=items')

    def mounts(self,
               server="eu",
               realm="archimonde",
               characterName="Protòtype",
               locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=mounts')

    def pets(self,
             server="eu",
             realm="archimonde",
             characterName="Protòtype",
             locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=pets')

    def petSlots(self,
                 server="eu",
                 realm="archimonde",
                 characterName="Protòtype",
                 locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=petSlots')

    def professions(self,
                    server="eu",
                    realm="archimonde",
                    characterName="Protòtype",
                    locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=professions')

    def progression(self,
                    server="eu",
                    realm="archimonde",
                    characterName="Protòtype",
                    locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=progression')

    def pvp(self,
            server="eu",
            realm="archimonde",
            characterName="Protòtype",
            locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=pvp')

    def quests(self,
               server="eu",
               realm="archimonde",
               characterName="Protòtype",
               locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=quests')

    def reputation(self,
                   server="eu",
                   realm="archimonde",
                   characterName="Protòtype",
                   locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=reputation')

    def statistics(self,
                   server="eu",
                   realm="archimonde",
                   characterName="Protòtype",
                   locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=statistics')

    def stats(self,
              server="eu",
              realm="archimonde",
              characterName="Protòtype",
              locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=stats')

    def talents(self,
                server="eu",
                realm="archimonde",
                characterName="Protòtype",
                locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=talents')

    def titles(self,
               server="eu",
               realm="archimonde",
               characterName="Protòtype",
               locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=titles')

    def audit(self,
              server="eu",
              realm="archimonde",
              characterName="Protòtype",
              locale="en_US"):

        self.route = self.route.format(realm, characterName)

        return Fetcher.fetchData(
            server=server,
            locale=locale,
            route=self.route,
            params='fields=audit')
