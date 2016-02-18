from flask import Flask, render_template, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
	'sqlite:///' + os.path.join(basedir, 'data.sqlite') 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

def make_shell_context():
	return dict(app=app, db=db, Lis=Lis, Tasks=Tasks)
manager.add_command("shell", Shell(make_context=make_shell_context))

class ListForm(Form):
	title = StringField('List Title', validators=[Required()])
	submit = SubmitField('Submit')

class TaskForm(Form):
	body = StringField("Tasks", validators=[Required()])
	submit = SubmitField('Save')

@app.route('/', methods=['GET', 'POST'])
def index():
	title = None
	form = ListForm()
	if form.validate_on_submit():
		lis = Lis(title=form.title.data)
		db.session.add(lis)
		flash('You have made a new List')
		return redirect(url_for('.index'))
	form.title.data = Lis.Title
	return render_template('index.html', form=form)


@app.route('/task/<int:id>', methods=['GET', 'POST'])
def task(id):
	task = Lis.query.get_or_404(id)
	form = TaskForm()
	if form.validate_on_submit():
		tas = Tasks(body=form.body.data, lis=lis)
		db.session.add(tas)
		flash('Task added to List')
		return redirect(url_for('.task', lis=lis.id))
	form.body.data = Tasks.body
	return render_template('task.html', lists=[lis], form=form)

class Lis(db.Model):
	__tablename__ = 'lists'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True)
	tasks = db.relationship('Tasks', backref='lis', lazy='dynamic')

	def __repr__(self):
		return '<Title %r>' % self.title

class Tasks(db.Model):
	__tablename__ = 'tasks'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text(64), unique=True, index=True)
	done = db.Column(db.Boolean, default=False)
	lis_id = db.Column(db.Integer, db.ForeignKey('lists.id'))

	def __repr__(self):
		return '<Body %r>' % self.body


if __name__ == '__main__':
	manager.run()