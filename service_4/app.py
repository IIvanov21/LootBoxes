from flask import Flask, request,jsonify
import random
app=Flask(__name__)

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

@app.route('/get/rarity' ,methods=['POST'])
def combine_information():#Design for service 4
    weapon_type, weapon = list(request.json.items())[0]
    weapon_rarity_factor = rarity_weapon_factor[weapon_type][weapon]
    condition, skin = list(request.json.items())[1]
    skin_rarity_factor = rarity_skin_factor[condition][skin]

    rarity = round(((weapon_rarity_factor+skin_rarity_factor) / 2)*100,2)
    return jsonify(rarity)


if __name__ == '__main__':
    app.run(host='0.0.0.0')