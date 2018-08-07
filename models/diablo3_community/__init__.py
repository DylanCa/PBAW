from .Act import Act
from .ArtisanAndRecipe import ArtisanAndRecipe
from .CharacterClassAndSkill import CharacterClassAndSkill
from .Follower import Follower
from .Item import Item
from .ItemType import ItemType
from .Profile import Profile


class Diablo3Community():
    def __init__(self, apikey):
        self.act = Act(apikey)
        self.artisan_and_recipe = ArtisanAndRecipe(apikey)
        self.character_class_and_skill = CharacterClassAndSkill(apikey)
        self.follower = Follower(apikey)
        self.item = Item(apikey)
        self.item_type = ItemType(apikey)
        self.profile = Profile(apikey)
