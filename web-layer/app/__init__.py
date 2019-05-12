from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

application = Flask(__name__)
Bootstrap( application )
nav = Nav()

application.config.from_object( Config )

db = SQLAlchemy( application )
migrate = Migrate( application, db )

login_manager = LoginManager(application) 
login_manager.login_view = 'login'

from app import routes, models

# Defining navigation bars
@nav.navigation()
def main_navbar():
    return Navbar(
        'Recommendation App', 
        View('Home', 'home'), 
        View('Logout', 'logout'),
    )

nav.init_app( application )