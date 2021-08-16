from flask import url_for
from flask_testing import TestCase
import json
from service_2.app import app, weapons

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_weapon(self):

        for _ in range(20):
            response = self.client.get(url_for('random_weapon'))
            weapon_choice=json.loads(response.data.decode())
            weapon_type, weapon = list(weapon_choice.items())[0]

            self.assert200(response)
            self.assertIn(weapon_type, weapons)
            self.assertIn(weapon, weapons[weapon_type])
