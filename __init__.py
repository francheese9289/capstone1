'''The init file is what ultimately runs the entire app. Without it, nothing will happen. 
All the objects we've created - api, authentication, site, etc - come together in the init.'''
from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
#from restricted_views import restricted_views

app = Flask(__name__)

app.register_blueprint(site)
app.config.from_object(Config)
app.register_blueprint(auth)
#app.register_blueprint(restricted_views, url_prefix='/restricted')
