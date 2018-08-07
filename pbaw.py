from models.wow_community import WowCommunity


class Pbaw():
    def __init__(self, apikey=''):
        self.wowc = WowCommunity(apikey)
