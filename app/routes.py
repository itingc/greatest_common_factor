from flask import render_template
from app import app
from app.form import Form
from greatest_common_factor import GreatestCommonFactor



@app.route('/')
def index():
    return "Welcome!!!"


@app.route('/gcf')
def gcf():
    form = Form()
    return render_template('index.html', title='Greatest Common Factor', form=form)




