from .Act import Act
from .ArtisanAndRecipe import ArtisanAndRecipe
from .CharacterClassAndSkill import CharacterClassAndSkill
from .Follower import Follower
from .Item import Item
from .ItemType import ItemType
from .Profile import Profile


class Diablo3Community():
    def __init__(self):
        self.act = Act()
        self.artisan_and_recipe = ArtisanAndRecipe()
        self.character_class_and_skill = CharacterClassAndSkill()
        self.follower = Follower()
        self.item = Item()
        self.item_type = ItemType()
        self.profile = Profile()
