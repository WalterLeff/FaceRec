from application import app
from flask import render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from application.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from application.models import User
from flask import request
from werkzeug.urls import url_parse
from application.models import User
from application import db
from application.forms import RegistrationForm
from application.forms import CreateNewSessionForm
from application.models import Classrooms


#authentication
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#pages
@app.route('/')
@app.route('/index')
@login_required
def index():
    # user = {'username' : 'Wouter'}
    # posts = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     }
    # ]
    return render_template('index.html', title='Home')
    

@app.route('/createsession', methods=['GET', 'POST'])
def createSession():
    form = CreateNewSessionForm()
    return render_template('createsession.html', title= 'Create new session', form = form)

@app.route('/createdataset', methods=['GET', 'POST'])
def createdataset():
    return render_template('createdataset.html', title= 'Create datasets')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

@app.route('/api')
@login_required
def api():
    return render_template('api.html', title='API')