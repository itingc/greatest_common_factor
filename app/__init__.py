from flask import Flask
from config import Config
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dafawefawefeahtrdhdr'
app.config.from_object(Config)

app._static_folder = os.path.join(os.getcwd(), 'static')


from app import routes
