from flask import render_template, redirect, request, flash, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import application, db
from app.forms import LoginForm, RegisterUserForm
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

	args_dict = request.args.get('next')	
	application.logger.info(args_dict)

	if login_form.validate_on_submit():
		# Verify sent credentials and log the user. In case the credentials do not match, redirect to login after flashing an error.
		user = User.by_login(login=login_form.username.data)

		if user is None or not user.check_password(login_form.password.data):
			flash('Invalid user or password')
			return redirect( url_for('login') )

		login_user(user, remember=login_form.remember_me.data)

		next_page = request.args.get('next')
		
		args_dict = request.args.to_dict()
		
		application.logger.info(args_dict)
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

@application.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect( url_for('home') )

	register = RegisterUserForm()

	has_user = User.query.filter_by(
		login=register.username.data, 
		email=register.email.data, 
	).first()

	if has_user:
		flash('User already registered. Try to login, maybe?')

		return redirect( url_for('login') )

	if register.validate_on_submit():
		user = User(
				login=register.username.data, 
				firstname=register.firstname.data, 
				lastname=register.lastname.data, 
				email=register.email.data, 
				gender=register.gender.data, 
		)
		user.set_password(register.password.data) # Validated equalty on form

		db.session.add( user )
		db.session.commit()
		flash(" You are now registered! Try to login!")

		return redirect( url_for('home') )

	return render_template('register-user.html', title="New user", form=register)

@application.route('/recommendation', methods=['GET'])
def recommendation():
	password

@application.route('/evaluate/<movie_id>')
def evaluate(movie_id):
	pass