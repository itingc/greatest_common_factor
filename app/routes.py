from flask import render_template, flash
from app import app
from app.form import Form
from app.gcf_input import GcfInput
from app.gcf_manager import GcfManager

GCF_DB = 'gcf.sqlite'
gcf_manager =GcfManager(GCF_DB)

@app.route('/', methods=['GET', 'POST'])
def gcf():
    form = Form()
    if form.validate_on_submit():
        try:
            gcf_input = GcfInput(form.num1.data, form.num2.data)
            flash(f'GCF = {gcf.calculate_gcf()}')
        except ValueError as e:
            flash(str(e))
    return render_template('index.html', title='Greatest Common Factor', form=form)




