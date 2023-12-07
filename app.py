from flask import Flask
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

flask db init
flask db migrate -m "Initial migration."
flask db upgrade
