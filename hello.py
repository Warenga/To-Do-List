from flask import Flask, render_template, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	title = None
	form = ListForm()
	if form.validate_on_submit():
		title = form.title.data
		flash('You have made a new List')
		return redirect(url_for('.index', title=title))
	form.title.data = ''
	return render_template('index.html', form=form, title=title)

@app.route('/user/<title>')
def user(title):
	return render_template('user.html', title=title)


@app.route('/task', methods=['GET', 'POST'])
def task():
	form = TaskForm()
	if form.validate_on_submit():
		body = form.body.data
		flash('Task added to List')
		return redirect(url_for('.task', body=body))
	form.body.data = ''
	return render_template('task.html', form=form)


class ListForm(Form):
	title = StringField('List Title', validators=[Required()])
	submit = SubmitField('Submit')

class TaskForm(Form):
	body = StringField("Tasks", validators=[Required()])
	submit = SubmitField('Save')


if __name__ == '__main__':
	app.run(debug=True)