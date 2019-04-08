from flask import render_template, flash, request
from app import app
from app.form import Form
from app.greatest_common_factor import GreatestCommonFactor
import json


@app.route('/')
def gcf():
    return render_template('index.html')
# def gcf():
#     form = Form()
#     if form.validate_on_submit():
#         try:
#             gcf = GreatestCommonFactor(form.num1.data, form.num2.data)
#             flash(f'GCF = {gcf.calculate_gcf()}')
#             response = app.response_class(
#                 status=300,
#                 response=json.dumps({'First Number': form.num1.data, 'Second Number': form.num2.data}),
#                 mimetype='application/json'
#             )
#             return response
#         except ValueError as e:
#             flash(str(e))
#     return render_template('index.html', title='Greatest Common Factor', form=form)


@app.route('/gcf_result', methods=['POST'])
def gcf_result():
    num1 = request.form['num1']
    num2 = request.form['num2']
    gcf = GreatestCommonFactor(num1, num2)
    result = gcf.calculate_gcf()
    response = app.response_class(
                    status=200,
                    response=json.dumps({'First Number': num1, 'Second Number': num2, 'GCF': result}),
                    mimetype='application/json'
                )
    return response
