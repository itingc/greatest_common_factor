from flask import Flask
from config import Config
from greatest_common_factor import GreatestCommonFactor


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dafawefawefeahtrdhdr'
app.config.from_object(Config)

@app.route('/')
def index():
    return "Welcome!!!"


@app.route('/gcf')
def gcf():
    return "Greatest Common Factor"




if __name__ == "__main__":
    app.run()