from .Profile import Profile
from .Ladder import Ladder
from .DataRessources import DataRessources


class Sc2Community():
    def __init__(self, apikey):
        self.profile = Profile(apikey)
        self.ladder = Ladder(apikey)
        self.data_ressources = DataRessources(apikey)