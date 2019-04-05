from flask import render_template, flash
from app import app
from app.form import Form
from app.greatest_common_factor import  GreatestCommonFactor


@app.route('/', methods=['GET', 'POST'])
def gcf():
    form = Form()
    if form.validate_on_submit():
        gcf = GreatestCommonFactor(form.num1.data, form.num2.data)
        flash(f"GCF = {gcf.calculate_gcf()} ")
        print(f"GCF = {gcf.calculate_gcf()} ")
    return render_template('index.html', title='Greatest Common Factor', form=form)




