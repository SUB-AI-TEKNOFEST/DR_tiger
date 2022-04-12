import numpy as np

from flask import Flask, request, render_template
from model.model_ml import get_compound_list
from operations.cloud_operations import topological_link_prediction
app = Flask(__name__)
from visualize import html_saved
import csv

with open('diseases_names.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
""" """
import os
if os.path.exists("templates/visualization.html"):
  os.remove("templates/visualization.html")
  print("visualization deleted.")

else:
  print("visualization does not exist.")

@app.route('/')
def index():
    return render_template(
        'index.html',
        colours =data)


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    selected_diseases = list(request.form.values())

    print(f"selected : {selected_diseases}")
    #predicted_compounds = get_compound_list(diseases_list = [selected_diseases[0][2:len(selected_diseases[0])-2]])
    #topological_results = topological_link_prediction(disase_list = [selected_diseases[0][2:len(selected_diseases[0])-2]],compound_list=predicted_compounds)
    predicted_compounds = {'Compound::DB00745': -0.00038662006, 'Compound::DB01255': -0.0004425164, 'Compound::DB01041': -0.0005766802,
     'Compound::DB01224': -0.0006786369, 'Compound::DB00993': -0.00071947876}
    topological_results =  {'Compound::DB00745': -0.00038662006, 'Compound::DB01255': -0.0004425164, 'Compound::DB01041': -0.0005766802, 'Compound::DB01224': -0.0006786369, 'Compound::DB00993': -0.00071947876}

    print(f"ml model {predicted_compounds}")
    print(f" topological {topological_results}")
    print(f" len is {len(topological_results)}")
    #html_saved(disase_list= [selected_diseases[0][2:len(selected_diseases[0])-2]],compound_list=predicted_compounds)
    return render_template('second.html',ml_model = predicted_compounds,topo = topological_results,selected = selected_diseases)



if __name__=='__main__':

  app.run('0.0.0.0', port=5000)