from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    # StrinfField - Tipo de Field
    # DataRequired - Informa que o campo é obrigatório
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    rememberme = BooleanField("rememberme")