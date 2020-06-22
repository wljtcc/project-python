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

# Configurando Conexão com o Banco de Dados
DB_URL = os.getenv('DB_CONNECTION') + '://' + os.getenv('DB_USERNAME') + ':' + os.getenv('DB_PASSWORD') + '@' + os.getenv('DB_HOST') + ':' + os.getenv('DB_PORT') + '/' + os.getenv('DB_DATABASE')
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Instanciando DB
db = SQLAlchemy(app)

# Importando o default.py
from app.controllers import default