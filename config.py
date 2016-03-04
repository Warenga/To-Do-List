import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	DEBUG = True
	WTF_CSRF_ENABLED = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

	SQLALCHEMY_TRACK_MODIFICATIONS = True
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'email'
	MAIL_PASSWORD = 'password'


	@staticmethod
	def init_app(app):
		pass

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {

	'default': Config
	# 'TestingConfig': TestingConfig
	# 'ProductionConfig': ProductionConfig
	
	}
 