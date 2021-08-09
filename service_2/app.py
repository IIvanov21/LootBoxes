from flask import Flask
import random
app=Flask(__name__)

weapons = {'Snipers':['SSG 08','AWP','SCAR-20','G3SG1'],'Assault Rifles':['FAMAS','M4A1-S','AK-47','SG 553','AUG'],'SMG':['MP9','MAC-10','P90','MP7','UMP-45']}

@app.route('/get/weapon')
def random_weapon():#Design for service 2
    weapon_type = random.choice(list(weapons))
    weapon_name = random.choice(weapons[weapon_type])
    weapon_choice = {weapon_type:weapon_name}
    return weapon_choice

if __name__ == '__main__':
    app.run(host='0.0.0.0')