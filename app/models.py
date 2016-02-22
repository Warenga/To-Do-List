from . import db, login_manager
from flask import request
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	lists = db.relationship('Lis', backref='author', lazy='dynamic')

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

				
class Lis(db.Model):
	__tablename__ = 'lists'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=True)
	author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
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
		status = 'done' if self.done else 'open'
		return '<{0> tasks: {1} by {2}>'.format(
			status, self.done )

	def to_json(self):
		json_tasks = {
			'body': self.body,
			'done': self.done,
			'status': 'done' if self.done else 'open'
		}
		return json_tasks

	@staticmethod
	def from_json(json_tasks):
		Tasks(Json.loads(json_tasks)).save()