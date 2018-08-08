from models.wow_community import WowCommunity
from unittest import TestCase


class TestWowCommunity(TestCase):
    def setUp(self):
        self.wowc = WowCommunity('sk23u53qczcuxnv7p544dwrktm84sdy4')
        self.notEqual = {"status": "nok", "reason": "When in doubt, blow it up. (page not found)"}

    def test_achievement(self):
        self.assertNotEqual(self.notEqual, self.wowc.achievement.achievement())