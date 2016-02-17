from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

class ListForm(Form):
	Title = StringField('List Title', validators=[Required()])
	submit = SubmitField('Save')

class TaskForm(Form):
	body = StringField("Tasks", validators=[Required()])
	submit = SubmitField('Save')
