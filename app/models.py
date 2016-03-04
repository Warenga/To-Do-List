from . import db, login_manager
from flask import request
from flask import current_app, session, url_for, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from rauth import OAuth2Service



class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	lists = db.relationship('Lis', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {0}>'.formant(self.username)

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
	tasks = db.relationship('Tasks', backref='lis')


	def __repr__(self):
		return '<Title %r>' % self.title

class Tasks(db.Model):
	__tablename__ = 'tasks'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text(64), unique=True, index=True)
	done = db.Column(db.Boolean, default=False)
	lis_id = db.Column(db.Integer, db.ForeignKey('lists.id'))


