from flask import url_for
from flask_testing import TestCase
import json
from service_3.app import app, skins,conditions

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_skin(self):

        for _ in range(20):
            response = self.client.get(url_for('random_skin'))
            skin_choice=json.loads(response.data.decode())
            condition, skin = list(skin_choice.items())[0]

            self.assert200(response)
            self.assertIn(condition, conditions)
            self.assertIn(skin, skins)