from .Profile import Profile
from .Ladder import Ladder
from .DataRessources import DataRessources


class Sc2Community():
    def __init__(self):
        self.profile = Profile()
        self.ladder = Ladder()
        self.data_ressources = DataRessources()