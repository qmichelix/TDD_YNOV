from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from your_application_name.Book import db  # Importez db de votre fichier Book.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://utilisateur:mot_de_passe@localhost/nom_de_votre_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # Crée les tables si elles n'existent pas

# Autres configurations et routes de votre application
from flask import Flask
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

flask db init
flask db migrate -m "Initial migration."
flask db upgrade
