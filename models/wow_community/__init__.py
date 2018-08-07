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
    
    def __init__(self, apikey):
        self.achievement = Achievement(apikey)
        self.auction = Auction(apikey)
        self.boss = Boss(apikey)
        self.challenge_mode = ChallengeMode(apikey)
        self.character_profile = CharacterProfile(apikey)
        self.data_ressources = DataRessources(apikey)
        self.guild_profile = GuildProfile(apikey)
        self.item = Item(apikey)
        self.mount = Mount(apikey)
        self.pet = Pet(apikey)
        self.pvp = Pvp(apikey)
        self.quest = Quest(apikey)
        self.realm_status = RealmStatus(apikey)
        self.recipe = Recipe(apikey)
        self.spell = Spell(apikey)
        self.zone = Zone(apikey)
