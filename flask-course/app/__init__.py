import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '../')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

#app = Flask(os.getenv('FLASK_APP'))
app = Flask(os.getenv('FLASK_APP_NAME'))

# Instanciando DB
# db = SQLAlchemy(app)

# Importando o default.py
from app.controllers import default