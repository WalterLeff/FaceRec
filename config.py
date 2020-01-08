import os
from os import environ
import pyodbc
from sqlalchemy import create_engine
import urllib



basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    #general
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')

    #database
    params = urllib.parse.quote_plus(r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:facerec.database.windows.net,1433;Database=FaceRec;Uid=projectIV@facerec;Pwd=Project4;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    #conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False
    engine_azure = create_engine(SQLALCHEMY_DATABASE_URI,echo=True)

    print('Azure sql databse connection is ok')
    print(engine_azure.table_names())
