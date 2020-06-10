from flask import Flask


app = Flask(__name__)

# Importando o default.py
from app.controllers import default