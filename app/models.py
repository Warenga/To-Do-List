from . import db, login_manager
from flask import request, current_app, session, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	cards = db.relationship('Cards', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {0}>'.format(self.username)

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

		
class Cards(db.Model):
	__tablename__ = 'cards'
	id = db.Column(db.Integer, primary_key=True)
	card = db.Column(db.String(64), unique=True)
	author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	created_time = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
	tasks = db.relationship('Tasks', backref='card')


	def __repr__(self):
		return '<card %r>' % self.card

class Tasks(db.Model):
	__tablename__ = 'tasks'
	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.Text(64), index=True)
	done = db.Column(db.Boolean, default=False)
	card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))


	def __repr__(self):
		return '<task %r>' % self.task