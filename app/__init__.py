from flask import Flask
from config import Config
import os


app = Flask(__name__)

# Add simple security to prevent attack
app.config['SECRET_KEY'] = 'dafawefawefeahtrdhdr'
app.config.from_object(Config)

# Set directory for static folder
app._static_folder = os.path.join(os.getcwd(), 'static')


from app import routes
