from flask import render_template, flash
from app import app
from app.form import Form
from app.gcf import Gcf
from app.gcf_manager import GcfManager

GCF_DB = 'gcf.sqlite'
gcf_manager = GcfManager(GCF_DB)

@app.route('/', methods=['GET', 'POST'])
def gcf():
    form = Form()
    if form.validate_on_submit():
        try:
            gcf = Gcf(form.num1.data, form.num2.data)
            gcf_manager.add_gcf(gcf)
            flash(f'GCF = {gcf.calculate_gcf()}')
        except ValueError as e:
            flash(str(e))
    return render_template('index.html', title='Greatest Common Factor', form=form)




