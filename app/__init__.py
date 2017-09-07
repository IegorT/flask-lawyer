from flask import Flask
from flask_babel import Babel
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)
babel = Babel(app)

from app import view