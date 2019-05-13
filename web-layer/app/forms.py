from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    submit   = SubmitField('Sign In')
    remember_me = BooleanField('Remember Me')

class RegisterUserForm(FlaskForm):
    username  = StringField('Username', validators=[DataRequired()])
    firstname = StringField('First name', validators=[DataRequired()]) 
    lastname  = StringField('Last name', validators=[DataRequired()])
    email  = StringField('E-Mail', validators=[Length(min=6, max=100), Email()])
    gender = SelectField('Gender', choices=[('male', 'Masculino'), ('female', 'Feminino'), ('none', 'Nenhum/Não identificado')], validators=[DataRequired()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Save')

    def validade_username(self, username):
        user = User.by_login(login=username)

        if user is not None:
            raise ValidationError('Username/login taken. Please select a different one.')

        return True

    def validade_email(self, email):
        user = User.by_email(email=email)

        if user is not None:
            raise ValidationError('The e-mail provided is already in use. Please choose another one.')
        
        return True

class RedefinePassword(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')