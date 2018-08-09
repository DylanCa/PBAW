from models.wow_community import WowCommunity
from models.diablo3_community import Diablo3Community
from models.sc2_community import Sc2Community


class Pbaw:
    def WowC():
        return WowCommunity()

    def D3C():
        return Diablo3Community()

    def SC2C():
        return Sc2Community()
