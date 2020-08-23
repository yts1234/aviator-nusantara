#Import Flask and the other important library
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

#Objects instantiation
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

#data seeder
seeder = FlaskSeeder()
seeder.init_app(app, db)

#import internal modules
from app.model import flights
from app import routes
