import os
from application import app, db
from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from application.models import User
from application.forms import LoginForm, RegistrationForm, CreateNewSessionForm, CreateDataset
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class



######################################################
#Authentication:
######################################################
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

######################################################
#create dataset:
######################################################
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

@app.route('/createdata', methods=['GET', 'POST'])
@login_required
def createData():
	form = CreateDataset()
	ModuleName = form.Module.data
	# set session for image results
	if "file_urls" not in session:
		session['file_urls'] = []
	# list to hold our uploaded image urls
	file_urls = session['file_urls']

	# handle image upload from Dropszone
	if request.method == 'POST':
		file_obj = request.files
		for f in file_obj:
			file = request.files.get(f)
			
			# save the file with to our photos folder
			filename = photos.save(
				file,
				name=file.filename    
			)			
			# append image urls
			file_urls.append(photos.url(filename))
			
		session['file_urls'] = file_urls
		#return "uploading..."
		flash('Congratulations, photo''s are uploaded')
	# return dropzone template on GET request 
	return render_template('createdata.html', title='Create datasets', form=form,)

@app.route('/showdata')
@login_required
def showData():
	form = CreateDataset()
	# redirect to home if no images to display
	if "file_urls" not in session or session['file_urls'] == []:
		return redirect(url_for('index'))
		
	# set the file_urls and remove the session variable
	file_urls = session['file_urls']
	session.pop('file_urls', None)
	flash('Congratulations, photo''s are uploaded')
	return render_template('createdata.html', file_urls=file_urls, form=form)

######################################################
#Pages:
######################################################

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index(): 
	return render_template('index.html')

@app.route('/home')
@login_required
def home():
	return render_template('home.html', title = 'Home')

@app.route('/createsession')
@login_required
def createSession():
	return render_template('createsession.html', title= 'Create new session')

@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html', title='Dashboard')

######################################################
#azure blob storage:
######################################################
import os
from azure.storage.blob import BlockBlobService

@app.route('/blobStorage', methods=['GET', 'POST'])
def uploadToBlob():
	root_path = os.getcwd()
	dir_name = 'Data_upload2Blob'
	path = f"{root_path}/{dir_name}"
	file_names = os.listdir(path)

	account_key	 = 'Zc2lxyoAFOfCB4GMVRl7yqnHJ3QQGJohFXXI9NmVLGIJRWkzkgDgOxdnu7DnpXRNCnry3T0XFASLUQ9vLGDPWA=='
	account_name = 'facerecblob'
	container_name = 'students'


	block_blob_service = BlockBlobService(
	account_name=account_name,
	account_key=account_key
	)
	container_client = block_blob_service.create_container(container_name)

	for file_name in file_names:
		blob_name = f"{file_name}"
		file_path = f"{path}/{file_name}"
		block_blob_service.create_blob_from_path(container_name, blob_name, file_path)
	return render_template('createdata.html')

######################################################
#Machine learning:
######################################################
from AI.encode_faces import encode_faces

@app.route('/trainDataset')
@login_required
def trainData():
	encode_faces()
	return redirect('dashboard.html')
	

######################################################
#swagger API documentatie:  TODO: nice to have
######################################################

# @app.route('/api')
# @login_required
# def api():
# 	return render_template('api.html', title='API')