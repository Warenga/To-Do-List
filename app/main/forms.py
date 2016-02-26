from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, HiddenField
from wtforms.validators import Required

class ListForm(Form):
	title = StringField('Title')
	submit = SubmitField('Submit')


class TaskForm(Form):
	body = StringField('', validators=[Required()])
	submit = SubmitField('Submit')


