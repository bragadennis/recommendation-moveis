from flask import render_template, redirect, request, flash, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import application
from app.forms import LoginForm
from app.models import User
from werkzeug.urls import url_parse


@application.route('/')
def redirect_to_home_or_login():
	if not current_user.is_authenticated:
		# Redirect to login
		return redirect( url_for('login') )

	# Redirect to homepage
	return redirect( url_for('home') )

@application.route('/login', methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect( url_for('home') )

	login_form = LoginForm()

	if login_form.validate_on_submit():
		# Verify sent credentials and log the user. In case the credentials do not match, redirect to login after flashing an error.
		user = User.by_login(login=login_form.username.data)

		if user is None or not user.check_password(login_form.password.data):
			flash('Invalid user or password')
			return redirect( url_for('login') )

		login_user(user, remember=login_form.remember_me.data)

		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('home')
		
		return redirect( next_page )

	return render_template('login.html', title='Sign In', form=login_form)

@application.route('/logout')
def logout():
	logout_user()
	return redirect( url_for('login') ) 

@application.route('/home')
@login_required
def home():
	flash('For logged users only!') 
	return render_template('home.html', title="Home ")

@application.route('/another-home')
@login_required
def another_home():
	flash('For logged users only!')
	return render_template('another-home.html', title="Home ")