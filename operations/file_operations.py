import csv
import sys
sys.path.append("..")
COVID = ['Disease::SARS-CoV2 E',
'Disease::SARS-CoV2 M',
'Disease::SARS-CoV2 N',
'Disease::SARS-CoV2 Spike',
'Disease::SARS-CoV2 nsp1',
'Disease::SARS-CoV2 nsp10',
'Disease::SARS-CoV2 nsp11',
'Disease::SARS-CoV2 nsp12',
'Disease::SARS-CoV2 nsp13',
'Disease::SARS-CoV2 nsp14',
'Disease::SARS-CoV2 nsp15',
'Disease::SARS-CoV2 nsp2',
'Disease::SARS-CoV2 nsp4',
'Disease::SARS-CoV2 nsp5',
'Disease::SARS-CoV2 nsp5_C145A',
'Disease::SARS-CoV2 nsp6',
'Disease::SARS-CoV2 nsp7',
'Disease::SARS-CoV2 nsp8',
'Disease::SARS-CoV2 nsp9',
'Disease::SARS-CoV2 orf10',
'Disease::SARS-CoV2 orf3a',
'Disease::SARS-CoV2 orf3b',
'Disease::SARS-CoV2 orf6',
'Disease::SARS-CoV2 orf7a',
'Disease::SARS-CoV2 orf8',
'Disease::SARS-CoV2 orf9b',
'Disease::SARS-CoV2 orf9c',
'Disease::MESH:D045169',
'Disease::MESH:D045473',
'Disease::MESH:D001351',
'Disease::MESH:D065207',
'Disease::MESH:D028941',
'Disease::MESH:D058957',
'Disease::MESH:D006517']

entity_to_id = './entityToId.tsv'
relation_to_id = './relationToId.tsv'

allowed_drug = []
with open("./FDAApproved.tsv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t', fieldnames=['drug','ids'])
    for row_val in reader:
        allowed_drug.append(row_val['drug'])
        
def entity_relations(allowed_labels, what_diseases):
    entity_name_to_id = {}
    entity_id_to_name = {}
    relation_name_to_id = {}
    
    with open(entity_to_id, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t', fieldnames=['name','id'])
        for row_val in reader:
            entity_name_to_id[row_val['name']] = int(row_val['id'])
            entity_id_to_name[int(row_val['id'])] = row_val['name']
    
    with open(relation_to_id, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t', fieldnames=['name','id'])
        for row_val in reader:
            relation_name_to_id[row_val['name']] = int(row_val['id'])
    allowed_drug_ids = []
    disease_ids = []
    for drug in allowed_drug:
        allowed_drug_ids.append(entity_name_to_id[drug])

    for disease in what_diseases:
        disease_ids.append(entity_name_to_id[disease])

    allowed_relation_ids = [relation_name_to_id[treat]  for treat in allowed_labels]
    return entity_name_to_id, entity_id_to_name, relation_name_to_id, allowed_relation_ids, allowed_drug_ids, disease_ids


def open_file_return_list(file_name):
    with open(file_name,'r') as file:
        lines = [item.replace('\n','') for item in file.readlines()]
        return lines
