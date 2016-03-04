from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, HiddenField, validators
from wtforms.validators import Required

class ListForm(Form):
	title = StringField('New List', validators=[Required()])
	submit = SubmitField('Submit')


class TaskForm(Form):
	body = StringField('', validators=[Required()])
	submit = SubmitField('Save')


