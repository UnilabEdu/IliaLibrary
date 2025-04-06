from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('იუზერნეიმი', validators=[DataRequired()])
    password = PasswordField('პაროლი', validators=[DataRequired()])
    submit = SubmitField('დალოგინება')

    