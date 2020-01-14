import os
from os import environ
from flask_sqlalchemy import create_engine
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

	#general
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	FLASK_ENV='development'
	FLASK_APP='app'
	FLASK_DEBUG=1
	TESTING = environ.get('TESTING')
	FLASK_DEBUG = environ.get('FLASK_DEBUG') or True
	SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False

   # Dropzone settings
	DROPZONE_ALLOWED_FILE_CUSTOM = True
	DROPZONE_ALLOWED_FILE_TYPE = 'image/*'
	DROPZONE_UPLOAD_MULTIPLE = True
	DROPZONE_REDIRECT_VIEW = 'showData'#'showData'

	# Uploads settings
	UPLOADED_PHOTOS_DEST = os.getcwd() + '/Data_upload2Blob/'

	#azure sql database
	params = urllib.parse.quote_plus(r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:facerec.database.windows.net,1433;Database=FaceRec;Uid=projectIV@facerec;Pwd=Project4;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
	SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
	engine_azure = create_engine(SQLALCHEMY_DATABASE_URI,echo=True)

	#azure blob storage
	AZURE_STORAGE_ACCOUNT_NAME = 'facerecblob' 
	AZURE_STORAGE_ACCOUNT_KEY = 'ro3K4T0Jhcd1cx7X3rrFCzRztDk8IEdCkrH3'
	
	#AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=facerecblob;AccountKey=ro3K4T0Jhcd1cx7X3rrFCzRztDk8IEdCkrH3+lReOpX1mSFmDhuidH23lskLDMTwFpDJ1pGxZjWJqgt/KBx09Q==;EndpointSuffix=core.windows.net

	#Azure Cognitive Servoces
	FACE_SUBSCRIPTION_KEY='f07cad5607c04b01b2e0b38f0bbd3872'
	FACE_ENDPOINT = 'https://facerec-face-api.cognitiveservices.azure.com/'

	print('Azure sql databse connection is ok')
	#print(engine_azure.table_names())

print("All config settings have been read")