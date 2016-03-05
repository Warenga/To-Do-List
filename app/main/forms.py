# Contains forms used in main

from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField, BooleanField, validators
from wtforms.validators import Required

class CardForm(Form):
	card = StringField('New Card')
	submit = SubmitField('Save')

class TaskForm(Form):
	tasks = StringField('')
	submit = SubmitField('Submit')
