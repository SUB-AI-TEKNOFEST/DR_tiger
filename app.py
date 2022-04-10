import numpy as np

from flask import Flask, request, render_template
from model_ml import user_diseases_list
app = Flask(__name__)

import csv

with open('diseases_names.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)



@app.route('/')
def index():
    return render_template(
        'index.html',
        colours =data)


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    input_data = list(request.form.values())
    print(f"1 : {[input_data[0][1:len(input_data[0])]]}")
    result_diseases = user_diseases_list(diseases_list = [input_data[0][2:len(input_data[0])-2]])
    print(f"5 {result_diseases}")
    return render_template('second.html',colours = result_diseases)


if __name__ == '__main__':
    app.run(debug=True)