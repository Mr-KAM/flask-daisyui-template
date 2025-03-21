from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, PasswordField  # Updated TextField → StringField
from wtforms.validators import DataRequired  # Updated Required → DataRequired

class ExampleForm(FlaskForm):
    title = StringField(u'Título', validators=[DataRequired()])  # Fixed
    content = TextAreaField(u'Conteúdo')
    date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')

class LoginForm(FlaskForm):
    user = StringField(u'Username', validators=[DataRequired()])  # Fixed
    password = PasswordField(u'Password', validators=[DataRequired()])
