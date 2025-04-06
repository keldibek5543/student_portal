from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[InputRequired(), Length(min=3, max=50)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Пароль", validators=[InputRequired(), Length(min=6)])
    confirm = PasswordField("Повторите пароль", validators=[InputRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField("Зарегистрироваться")
