import os
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
#from flask_azure_storage import FlaskAzureStorage
from azure import storage
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
dropzone = Dropzone(app)
#azure_storage = FlaskAzureStorage(app)
manager = Manager(app)

if not app.debug:

	if not os.path.exists('logs'):
		os.mkdir('logs')
	file_handler = RotatingFileHandler('logs/website.log', maxBytes=10240,
									   backupCount=10)
	file_handler.setFormatter(logging.Formatter(
		'%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)

	app.logger.setLevel(logging.INFO)
	app.logger.info('website startup')

from application import routes, models, errors, forms

if __name__ == '__main__':
	# * --- DEBUG MODE: --- *
	app.run(host='0.0.0.0', port=5000, debug=True)
	