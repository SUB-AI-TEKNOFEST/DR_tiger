import numpy as np
import os
from flask import Flask, request, render_template
from model.model_ml import get_compound_list
from operations.cloud_operations import topological_link_prediction
app = Flask(__name__)
from visualize import html_saved
import csv
with open('diseases_names.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    
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

@app.route('/predict', methods =["GET", "POST"])
def predict():
    selected_diseases = request.form['manu']
    print(f"selected : {selected_diseases}")
    print(f"given disease  : {[selected_diseases[2:len(selected_diseases)-2]]}")
    # predicted_compounds = get_compound_list(diseases_list=[selected_diseases[2:len(selected_diseases)-2]])
    # topological_results = topological_link_prediction( disase_list=[selected_diseases[2:len(selected_diseases)-2]], compound_list=predicted_compounds)

    predicted_compounds = {'Compound::DB14128': -0.0050533684, 'Compound::DB09341': -0.0051014163, 'Compound::DB00815': -0.005489906, 'Compound::DB12028': -0.005498439}

    topological_results = {'SARS-CoV2 E::DB14128': {'tg_adamic_adar': 0, 'tg_common_neighbors': 0, 'tg_preferential_attachment': 0, 'tg_total_neighbors': 6, 'tg_resource_allocation': 0}, 'SARS-CoV2 E::DB09341': {'tg_adamic_adar': 0, 'tg_common_neighbors': 0, 'tg_preferential_attachment': 0, 'tg_total_neighbors': 6, 'tg_resource_allocation': 0}, 'SARS-CoV2 E::DB00815': {'tg_adamic_adar': 0, 'tg_common_neighbors': 0, 'tg_preferential_attachment': 24, 'tg_total_neighbors': 10, 'tg_resource_allocation': 0}, 'SARS-CoV2 E::DB12028': {'tg_adamic_adar': 0, 'tg_common_neighbors': 0, 'tg_preferential_attachment': 0, 'tg_total_neighbors': 6, 'tg_resource_allocation': 0}}

    topological_result_array_form = []
    for key,value in topological_results.items():
        value_str = str(value).replace('{','').replace('}','').split(',')
        key_str =str(key)
        topological_result_array_form.append(key_str)
        for v in value_str:
            topological_result_array_form.append(v)
    print(f"ml model {predicted_compounds}")
    print(f" topological {topological_results}")
    print(f" len is {len(topological_results)}")
    html_saved(disase_list= [selected_diseases[2:len(selected_diseases)-2]],compound_list=predicted_compounds)
    return render_template('second.html',ml_model = predicted_compounds,topo = topological_result_array_form ,selected = selected_diseases)

@app.route('/visualize', methods =["GET", "POST"])
def visualize():
    return render_template('visualization.html')

if __name__=='__main__':
    app.run('0.0.0.0', port=5000)