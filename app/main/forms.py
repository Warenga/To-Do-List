# Contains forms used in main

from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField, PasswordField, BooleanField, validators
from wtforms.validators import Required, Email, Length, EqualTo

class CardForm(Form):
	card = StringField('New Card')
	submit = SubmitField('Save')

class TaskForm(Form):
	tas = StringField('')
	submit = SubmitField('Submit')

class UserForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	username = StringField('Username', validators=[Required(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Register')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')

	