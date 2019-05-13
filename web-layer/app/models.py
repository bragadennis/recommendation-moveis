from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import login_manager
import uuid

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	uuid = db.Column(db.String, index=True, unique=True, default=uuid.uuid4().__str__() )
	login     = db.Column(db.String(64), index=True, unique=True)
	password  = db.Column(db.String(128))
	firstname = db.Column(db.String(64), nullable=True)
	lastname  = db.Column(db.String(64), nullable=True)
	gender    = db.Column(db.String(10), nullable=True)
	email     = db.Column(db.String(100), nullable=True, unique=True)


	def __repr__( self ):
		return '<User login: {}, UUID: {}, ID: {}>'.format(self.login, self.uuid, self.id)

	def check_password(self, password_attempt):
		return check_password_hash(self.password, password_attempt)

	# Debug purpose only
	def set_password(self, password):
		self.password = generate_password_hash(password)

	@staticmethod
	def by_login(login):
		return User.query.filter_by(login=login).first()

	@staticmethod
	def by_email(email):
		return User.query.filter_by(email=email).first()

@login_manager.user_loader
def load_user(id):
	return User.query.get( int(id) ) # Review the possibility of using the UUID
