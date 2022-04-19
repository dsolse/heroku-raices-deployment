from flask import Flask
from routes.main.main import main
from routes.admin.admin import admin
# Servicios
from utils_app.login_manager import login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object("config.BaseConfig")

app.register_blueprint(admin)
app.register_blueprint(main)

# servicios
Bcrypt(app)
SQLAlchemy(app)
login_manager.init_app(app)