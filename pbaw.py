from models.wow_community import WowCommunity
from models.diablo3_community import Diablo3Community


class Pbaw():
    def __init__(self, apikey=''):
        self.wowc = WowCommunity(apikey)
        self.d3c = Diablo3Community(apikey)
