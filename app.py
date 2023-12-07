from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from LIVRE.Book import db  # Assurez-vous que ce chemin d'importation est correct

app = Flask(__name__)

# Assurez-vous que cette URI de base de données est correcte et correspond à votre configuration CI/CD
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://utilisateur:mot_de_passe@localhost/nom_de_votre_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Cette partie est nécessaire uniquement si vous souhaitez créer des tables lors du démarrage de l'application
with app.app_context():
    db.create_all()

# Autres configurations et routes de votre application

