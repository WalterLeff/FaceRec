from application import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from application import login


import sqlite3
from flask import _app_ctx_stack

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
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

class ClassSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teachersname = db.Column(db.String(128), index=True, unique=False)
    classroom = db.Column(db.String(128), index=True, unique=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey('classrooms.id'))

    def __repr__(self):
        return '<Classroom {}>'.format(self.classroom)

class Classrooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classroomname = db.Column(db.String(128), index=True, unique=True)
    classroomnumber = db.Column(db.String(64), index=True, unique=True)


    def __repr__(self):
        return '<Classroom {}>'.format(self.classroomname)

class Teacher(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      teachersname = db.Column(db.String(128), index=True, unique=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)