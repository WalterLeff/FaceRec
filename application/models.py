from application import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from application import login
import sqlite3
from flask import _app_ctx_stack

# import pyodbc
# from sqlalchemy import create_engine
# import urllib

# #urllib.parse.quote_plus for python 3
# params = urllib.parse.quote_plus(r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:facerec.database.windows.net,1433;Database=FaceRec;Uid=projectIV@facerec;Pwd=Project4;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
# conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
# engine_azure = create_engine(conn_str,echo=True)

# print('connection is ok')
# print(engine_azure.table_names())

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):

    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Classrooms(db.Model):

    __tablename__ = 'Classrooms'
    id = db.Column(db.Integer, primary_key=True)
    classroomname = db.Column(db.String(128), index=True, unique=True)
    classroomnumber = db.Column(db.String(64), index=True, unique=True)


    def __repr__(self):
        return '<Classroom {}>'.format(self.classroomname)

class ClassSession(db.Model):

    __tablename__ = 'ClassSessions'
    id = db.Column(db.Integer, primary_key=True)
    teachersname = db.Column(db.String(128), index=True, unique=False)
    classroom = db.Column(db.String(128), index=True, unique=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey('Classrooms.id'))

    def __repr__(self):
        return '<ClassSessions {}>'.format(self.classroom)

class Teacher(db.Model):

    __tablename__ = 'Teacher'
    id = db.Column(db.Integer, primary_key=True)
    teachersname = db.Column(db.String(128), index=True, unique=True)

class Post(db.Model):

    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)