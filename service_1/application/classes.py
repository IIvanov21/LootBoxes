from application import db
from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField,IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class CustomWeapon(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    weapon_name = db.Column(db.String(30))
    weapon_type = db.Column(db.String(30))
    skin_name = db.Column(db.String(30))
    condition = db.Column(db.String(30))
    rarity = db.Column(db.Decimal)

class ShowWeapon(FlaskForm):
    weapon_name = StringField("Weapon Name:")
    weapon_type = StringField("Weapon Type:")
    skin_name = StringField("Skin Name:")
    rarity = DecimalField("Rarity:")
    condition = StringField("Condition:")
    submit = SubmitField("Generate Custom Weapon")
