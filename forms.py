from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    user_name = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email адрес', validators=[DataRequired(), Email()])
    password_hash = PasswordField('Пароль', validators=[DataRequired()])
    confirm = PasswordField('Повторите пароль', validators=[DataRequired()])
    accept_tos = BooleanField('Я принимаю лицензионное соглашение', validators=[DataRequired()])
    submit = SubmitField('Создать учетную запись')


class AddCarForm(FlaskForm):
    model = StringField('ФИО', validators=[DataRequired()])
    price = IntegerField('Уровень', validators=[DataRequired()])
    power = IntegerField('Класс:', validators=[DataRequired()])
    color = StringField('Содержание:', validators=[DataRequired()])
    dealer_id = SelectField('Номер школы', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Добавить портфолио')


class AddDealerForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    submit = SubmitField('Добавить новую школу')


class SearchPriceForm(FlaskForm):
    start_price = IntegerField('Минимальный уровень портфолио', validators=[DataRequired()], default=1000)
    end_price = IntegerField('Максимальный уровень портфолио', validators=[DataRequired()], default=10000)
    submit = SubmitField('Поиск')


class SearchDealerForm(FlaskForm):
    dealer_id = SelectField('Выбор школы', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Поиск')