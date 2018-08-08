from models.sc2_community import Sc2Community
from unittest import TestCase


class TestSC2Community(TestCase):
    def setUp(self):
        self.sc2c = Sc2Community('sk23u53qczcuxnv7p544dwrktm84sdy4')

    def test_profile(self):
        self.assertNotEqual({
            "status": "nok",
            "code": 404,
            "message": "Resource Not Found"
        }, self.sc2c.profile.profile())

    def test_ladders(self):
        self.assertNotEqual({
            "status": "nok",
            "code": 404,
            "message": "Resource Not Found"
        }, self.sc2c.profile.ladders())

    def test_matchHistory(self):
        self.assertNotEqual({
            "status": "nok",
            "code": 404,
            "message": "Resource Not Found"
        }, self.sc2c.profile.matchHistory())
