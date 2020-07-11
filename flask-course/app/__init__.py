import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand

# load dotenv in the base root
# APP_ROOT = os.path.join(os.path.dirname(__file__), '../')
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)

#app = Flask(os.getenv('FLASK_APP'))
app = Flask(__name__)
app.config.from_object('config')

# Instanciando DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
SERVER_RUN = Server(host=app.config['HOST'], port=app.config['PORT'])
manager.add_command('runserver', SERVER_RUN)
manager.add_command('db', MigrateCommand)

# Importando o default.py
from app.controllers import default
from app.controllers import login