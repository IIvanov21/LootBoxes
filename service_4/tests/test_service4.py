from flask import url_for
from flask_testing import TestCase
import json
from service_4.app import app, rarity_weapon_factor,rarity_skin_factor
import random

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_combine_information(self):
        weapon_type=random.choice(list(rarity_weapon_factor))
        weapon=random.choice(list(rarity_weapon_factor[weapon_type]))
        weapon_rarity=rarity_weapon_factor[weapon_type][weapon]
        condition=random.choice(list(rarity_skin_factor))
        skin=random.choice(list(rarity_skin_factor[condition]))
        skin_rarity=rarity_skin_factor[condition][skin]
        weapon_info= {weapon_type:weapon,condition:skin}

        response = self.client.post(url_for('combine_information'),json=weapon_info)

        rarity = round(((weapon_rarity+skin_rarity) / 2)*100,2)
        if rarity > 0: return "true"