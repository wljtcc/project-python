import os
from app import app
from flask import Flask

# Quando não vier a variavel
@app.route('/test/', defaults={'name':None})
@app.route('/test/<name>')
def test(name):
    if name:
        return "Name: %s" % name
    else:
        return "Test withut name"
    
# Passando e forçando um tipo de variável
@app.route('/perfil/<int:id>')
def perfil(id):
    return "Perfil: %s" % id
