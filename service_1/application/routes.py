from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask import Flask, render_template, request
from wtforms import SubmitField
from application import app, db
from application.classes import CustomWeapon, ShowWeapon
from sqlalchemy import asc, desc
import requests
import random


def random_skin():#Design for service 3
    skins = ['Printstream','Neo-Noir','Cyber Security','Monster Mashup', 'Fairy Tale','Hyperbeast']
    conditions = ['Factory New', 'Minimal Wear', 'Field_Tested', 'Well-Worn', 'Battle-Scarred']
    skin = random.choice(skins)
    condition = random.choice(conditions)
    skin_choice = {condition:skin}
    return skin_choice

def combine_information(weapon_choice,skin_choice):#Design for service 4
    # Scale factor is 1
    rarity_weapon_factor = {
    'Snipers':
    {'SSG 08':0.75,'AWP':0.2,'SCAR-20':0.9,'G3SG1':0.6},
    'Assault Rifles':
    {'FAMAS':0.9,'M4A1-S':0.5,'AK-47':0.55,'SG 553':0.7,'AUG':0.85},
    'SMG':
    {'MP9':0.2,'MAC-10':0.35,'P90':0.55,'MP7':0.1,'UMP-45':0.3}}
    rarity_skin_factor = {
    'Factory New':
    {'Printstream':0.2,'Neo-Noir':0.3,'Cyber Security':0.1,'Monster Mashup':0.25, 'Fairy Tale':0.1,'Hyperbeast':0.5}, 
    'Minimal Wear':
    {'Printstream':0.3,'Neo-Noir':0.4,'Cyber Security':0.25,'Monster Mashup':0.3, 'Fairy Tale':0.2,'Hyperbeast':0.55},
     'Field_Tested':
    {'Printstream':0.45,'Neo-Noir':0.55,'Cyber Security':0.4,'Monster Mashup':0.35, 'Fairy Tale':0.28,'Hyperbeast':0.68},
    'Well-Worn':
    {'Printstream':0.55,'Neo-Noir':0.6,'Cyber Security':0.45,'Monster Mashup':0.45, 'Fairy Tale':0.3,'Hyperbeast':0.72},
    'Battle-Scarred':
    {'Printstream':0.72,'Neo-Noir':0.8,'Cyber Security':0.55,'Monster Mashup':0.60, 'Fairy Tale':0.35,'Hyperbeast':0.88}}
    
    weapon_type, weapon = list(weapon_choice.items())[0]
    weapon_rarity_factor = rarity_weapon_factor[weapon_type][weapon]
    condition, skin = list(skin_choice.items())[0]
    skin_rarity_factor = rarity_skin_factor[condition][skin]

    rarity = round(((weapon_rarity_factor+skin_rarity_factor) / 2)*100,2)

    return rarity


@app.route('/',methods=['GET','POST'])
def index():
    error=""   
    
    show_form=ShowWeapon()
    show_form_one=ShowWeapon()
    show_form_two=ShowWeapon()
    show_form_three=ShowWeapon()

    if request.method=="POST":
        #Service 2: Get the weapon
        weapon_choice=requests.get('http://10.154.0.8:5001/get/weapon')
        weapon_choice=weapon_choice.json()
        weapon_type, weapon = list(weapon_choice.items())[0]
        #Service 3: Get the skin
        skin_choice=random_skin()
        condition, skin = list(skin_choice.items())[0]
        #Service 4: Generate rarity
        #rarity=combine_information(weapon_choice,skin_choice)
        #Store all the information in the table
        new_weapon=CustomWeapon(weapon_name=weapon,weapon_type=weapon_type,skin_name=skin,condition=condition,rarity=0)
        db.session.add(new_weapon)
        db.session.commit()
        #Create simple form to display the data in the html file 
        show_form.weapon_name.data = weapon
        show_form.weapon_type.data = weapon_type
        show_form.skin_name.data = skin
        show_form.condition.data = condition
        show_form.rarity.data = 0

        weapons=db.session.query(CustomWeapon).order_by(CustomWeapon.id.desc())
        if weapons.count() > 1 : 
            show_form_one.weapon_name.data = weapons[1].weapon_name
            show_form_one.weapon_type.data = weapons[1].weapon_type
            show_form_one.skin_name.data = weapons[1].skin_name
            show_form_one.condition.data = weapons[1].condition
            show_form_one.rarity.data = weapons[1].rarity
        if weapons.count() > 2 : 
            show_form_two.weapon_name.data = weapons[2].weapon_name
            show_form_two.weapon_type.data = weapons[2].weapon_type
            show_form_two.skin_name.data = weapons[2].skin_name
            show_form_two.condition.data = weapons[2].condition
            show_form_two.rarity.data = weapons[2].rarity
        if weapons.count() > 3 : 
            show_form_three.weapon_name.data = weapons[3].weapon_name
            show_form_three.weapon_type.data = weapons[3].weapon_type
            show_form_three.skin_name.data = weapons[3].skin_name
            show_form_three.condition.data = weapons[3].condition
            show_form_three.rarity.data = weapons[3].rarity
    return render_template('showLayout.html',show_form=show_form,show_form_one=show_form_one,show_form_two=show_form_two,show_form_three=show_form_three,message=error)


    