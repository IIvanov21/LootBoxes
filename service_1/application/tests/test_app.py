from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.classes import CustomWeapon
import requests_mock

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False)

        return app

    def setUp(self):
        db.create_all()
        new_weapon=CustomWeapon(weapon_name='AWP',weapon_type='Snipers',skin_name='Hyperbeast',condition='Factory New', rarity=20.2)
       
        db.session.add(new_weapon)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):
    def test_read(self):
        response=self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Weapon Type',response.data)
    
    def test_services(self):
        #Add entries to test the history functionality of the app
        new_weapon=CustomWeapon(weapon_name='AWP',weapon_type='Snipers',skin_name='Hyperbeast',condition='Factory New', rarity=20.2)
        new_weapon_one=CustomWeapon(weapon_name='SSG8',weapon_type='Snipers',skin_name='Debonair',condition='Minimal Wear', rarity=33.2)
        new_weapon_two=CustomWeapon(weapon_name='P90',weapon_type='SMG',skin_name='Aston',condition='Battle-Scared', rarity=59.8)

        db.session.add(new_weapon)
        db.session.add(new_weapon_one)
        db.session.add(new_weapon_two)
        db.session.commit()

        #Mock the actual services to get the desired reponses
        with requests_mock.Mocker() as m:
            response=self.client.get(url_for('index'))
            m.get('http://service_2:5000/get/weapon',json={'Snipers':'AWP'})
            m.get('http://service_3:5000/get/skin', json={'Factory New': 'Fairy Tale'})
            m.post('http://service_4:5000/get/rarity',json=20.2)
            response=self.client.post(url_for('index'),data='',follow_redirects=True)
        #Test the information displayed from the reponse
        self.assert200(response)
        self.assertIn('Weapon Name:',response.data.decode())
        self.assertIn('AWP',response.data.decode())
        self.assertIn('Weapon Type:',response.data.decode())
        self.assertIn('Snipers',response.data.decode())
        self.assertIn('Skin Name:',response.data.decode())
        self.assertIn('Fairy Tale',response.data.decode())
        self.assertIn('Rarity:',response.data.decode())
        self.assertIn('20.2',response.data.decode())
    
    #Additional test to ensure the functionality works consitantly without any history.
    def test_services_two(self):
        with requests_mock.Mocker() as m:
            response=self.client.get(url_for('index'))
            m.get('http://service_2:5000/get/weapon',json={'SMG':'P90'})
            m.get('http://service_3:5000/get/skin', json={'Battle-Scarred': 'Assimov'})
            m.post('http://service_4:5000/get/rarity',json=60.5)
            response=self.client.post(url_for('index'),data='',follow_redirects=True)

        self.assert200(response)
        self.assertIn('Weapon Name:',response.data.decode())
        self.assertIn('P90',response.data.decode())
        self.assertIn('Weapon Type:',response.data.decode())
        self.assertIn('SMG',response.data.decode())
        self.assertIn('Skin Name:',response.data.decode())
        self.assertIn('Assimov',response.data.decode())
        self.assertIn('Condition:',response.data.decode())
        self.assertIn('Battle-Scarred',response.data.decode())
        self.assertIn('Rarity:',response.data.decode())
        self.assertIn('60.5',response.data.decode())


            