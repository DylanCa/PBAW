import requests


class Profile():
    def __init__(self, apikey=''):
        self.apikey = apikey

    def getApiAccount(self,
                      server="eu",
                      account="Prototype#2971",
                      locale="en_US"):
        accountName = account.split("#")[0]
        accountNumber = account.split("#")[1]

        url = 'https://{}.api.battle.net/d3/profile/{}%23{}/?locale={}&apikey={}'.format(
            server, accountName, accountNumber, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def getApiHero(self,
                   server="eu",
                   account="Prototype#2971",
                   hero="109407264",
                   locale="en_US"):
        accountName = account.split("#")[0]
        accountNumber = account.split("#")[1]

        url = 'https://{}.api.battle.net/d3/profile/{}%23{}/hero/{}?locale={}&apikey={}'.format(
            server, accountName, accountNumber, hero, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def getApiDetailedHeroItems(self,
                                server="eu",
                                account="Prototype#2971",
                                hero="109407264",
                                locale="en_US"):
        accountName = account.split("#")[0]
        accountNumber = account.split("#")[1]

        url = 'https://{}.api.battle.net/d3/profile/{}%23{}/hero/{}/items?locale={}&apikey={}'.format(
            server, accountName, accountNumber, hero, locale, self.apikey)

        response = requests.get(url)

        return response.text

    def getApiDetailedFollowerItems(self,
                                    server="eu",
                                    account="Prototype#2971",
                                    hero="109407264",
                                    locale="en_US"):
        accountName = account.split("#")[0]
        accountNumber = account.split("#")[1]

        url = 'https://{}.api.battle.net/d3/profile/{}%23{}/hero/{}/follower-items?locale={}&apikey={}'.format(
            server, accountName, accountNumber, hero, locale, self.apikey)

        response = requests.get(url)

        return response.text
