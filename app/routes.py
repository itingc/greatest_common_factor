from flask import render_template, request
from app import app
from app.greatest_common_factor import GreatestCommonFactor
import json

''' Front page with a form to input two integers'''
@app.route('/')
def gcf():
    return render_template('index.html')


''' Calculate the result and save the data as json'''
@app.route('/gcf_result', methods=['POST'])
def gcf_result():
    num1 = request.form['num1']
    num2 = request.form['num2']
    try:
        gcf = GreatestCommonFactor(num1, num2)
        result = gcf.calculate_gcf()
        response = app.response_class(
                        status=200,
                        response=json.dumps({'First Number': int(num1), 'Second Number': int(num1), 'GCF': result}),
                        mimetype='application/json'
        )
    except ValueError as e:
        response = app.response_class(
            status=400,
            response=str(e)
        )

    return response
