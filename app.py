import numpy as np

from flask import Flask, request, render_template

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
    print(input_data)
    return render_template('second.html')


if __name__ == '__main__':
    app.run(debug=True)