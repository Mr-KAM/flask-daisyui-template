from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, PasswordField  # Updated TextField → StringField
from wtforms.validators import DataRequired  # Updated Required → DataRequired

class ExampleForm(FlaskForm):
    title = StringField(u'Titre', validators=[DataRequired()])  # Fixed
    content = TextAreaField(u'Contenu')
    date = DateTimeField(u'Date', format='%d/%m/%Y %H:%M')

class LoginForm(FlaskForm):
    user = StringField(u'Utilisateur', validators=[DataRequired()])  # Fixed
    password = PasswordField(u'Mot de passe', validators=[DataRequired()])
