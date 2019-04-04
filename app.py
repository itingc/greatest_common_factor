from flask import Flask
from greatest_common_factor import GreatestCommonFactor
app = Flask(__name__)


@app.route('/')
def gcf():
    return


if __name__ == '__main__':
    app.run()
