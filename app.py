import numpy as np

from flask import Flask, request, render_template
from model_ml import get_compound_list
from cloud_operations import topological_link_prediction
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
    selected_diseases = list(request.form.values())
    print(f"selected : {selected_diseases}")
    predicted_compounds = get_compound_list(diseases_list = [selected_diseases[0][2:len(selected_diseases[0])-2]])
    topological_results = topological_link_prediction(disase_list = predicted_compounds)
    print(f"ml model {predicted_compounds}")
    print(f" topological {topological_results}")
    return render_template('second.html',colours = selected_diseases)

if __name__=='__main__':
  app.debug=True
  app.run('0.0.0.0', port=5005)