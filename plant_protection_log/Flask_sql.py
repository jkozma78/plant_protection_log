from flask import Flask
from flask_sqlalchemy import SQLAlchemy


pp = Flask(__name__)
pp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pp.db'
pp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(pp)


class PlantProtectionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dated = db.Column(db.String(20), nullable=False)
    chemical = db.Column(db.String(200), nullable=False)
    plant = db.Column(db.String(250), nullable=False)
    area = db.Column(db.String(10), nullable=False)
    comment = db.Column(db.String(250))
