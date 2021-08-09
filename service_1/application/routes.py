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




@app.route('/',methods=['GET','POST'])
def index():
    error=""   
    
    show_form=ShowWeapon()
    show_form_one=ShowWeapon()
    show_form_two=ShowWeapon()
    show_form_three=ShowWeapon()

    if request.method=="POST":
        #Service 2: Get the weapon
        weapon_choice=requests.get('http://service_2:5000/get/weapon')
        weapon_choice=weapon_choice.json()
        weapon_type, weapon = list(weapon_choice.items())[0]
        #Service 3: Get the skin
        skin_choice=requests.get('http://service_3:5000/get/skin')
        skin_choice=skin_choice.json()
        condition, skin = list(skin_choice.items())[0]
        #Service 4: Generate rarity
        weapon_info={weapon_type:weapon, condition:skin}
        rarity=requests.post('http://service_4:5000/get/rarity',json=weapon_info).json()
        #Store all the information in the table
        new_weapon=CustomWeapon(weapon_name=weapon,weapon_type=weapon_type,skin_name=skin,condition=condition,rarity=rarity)
        db.session.add(new_weapon)
        db.session.commit()
        #Create simple form to display the data in the html file 
        show_form.weapon_name.data = weapon
        show_form.weapon_type.data = weapon_type
        show_form.skin_name.data = skin
        show_form.condition.data = condition
        show_form.rarity.data = rarity

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


    