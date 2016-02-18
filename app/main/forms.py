from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

class ListForm(Form):
	title = StringField('Title', validators=[Required()])
	submit = SubmitField('Save')

class TaskForm(Form):
	body = StringField('', validators=[Required()])
	submit = SubmitField('Save')
