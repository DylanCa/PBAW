from .Achievement import Achievement
from .Auction import Auction
from .Boss import Boss
from .ChallengeMode import ChallengeMode
from .CharacterProfile import CharacterProfile
from .DataRessources import DataRessources
from .GuildProfile import GuildProfile
from .Item import Item
from .Mount import Mount
from .Pet import Pet
from .Pvp import Pvp
from .Quest import Quest
from .RealmStatus import RealmStatus
from .Recipe import Recipe
from .Spell import Spell
from .Zone import Zone


class WowCommunity():
    def __init__(self):
        self.achievement = Achievement()
        self.auction = Auction()
        self.boss = Boss()
        self.challenge_mode = ChallengeMode()
        self.character_profile = CharacterProfile()
        self.data_ressources = DataRessources()
        self.guild_profile = GuildProfile()
        self.item = Item()
        self.mount = Mount()
        self.pet = Pet()
        self.pvp = Pvp()
        self.quest = Quest()
        self.realm_status = RealmStatus()
        self.recipe = Recipe()
        self.spell = Spell()
        self.zone = Zone()
