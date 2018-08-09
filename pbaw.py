from models.wow_community import WowCommunity
from models.diablo3_community import Diablo3Community
from models.sc2_community import Sc2Community


class Pbaw:

    def WowC(self, apikey=''):
        return WowCommunity(apikey)

    def D3C(self, apikey=''):
        return Diablo3Community(apikey)

    def SC2C(self, apikey=''):
        return Sc2Community(apikey)
