from flask import Flask
import random
app=Flask(__name__)

skins = ['Printstream','Neo-Noir','Cyber Security','Monster Mashup', 'Fairy Tale','Hyperbeast']
conditions = ['Factory New', 'Minimal Wear', 'Field_Tested', 'Well-Worn', 'Battle-Scarred']

@app.route('/get/skin')
def random_skin():#Design for service 3
    skin = random.choice(skins)
    condition = random.choice(conditions)
    skin_choice = {condition:skin}
    return skin_choice


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)