import pyTigerGraph as tg
import pandas as pd
import sys
sys.path.append("..")
from operations import file_operations

secret="ji08rpup1652lum47ojvpuei1ievolum"
host="https://offlabel.i.tgcloud.io"  
graphname="DRKG"
username="tigergraph" 
password="utku123"

try:
    graph = tg.TigerGraphConnection(host=host, graphname=graphname)
    authToken = graph.getToken(secret=secret)
    authToken = authToken[0]
    conn = tg.TigerGraphConnection(host=host,graphname=graphname,username=username,password=password,apiToken=authToken)
except Exception as e:
    print('Tigergraph')
# for i in range(636018,len(triplets)):
#     [h,r,t] = triplets[i]
#     h_type = h.split("::")[0].replace(" " ,"")
#     h_id = str(h.split("::")[1])
#     t_type = t.split("::")[0].replace(" " ,"")
#     t_id = str(t.split("::")[1])
#     replaced = r.replace(" ","").replace(":","").replace("+","").replace(">","").replace("-","")   
#     print(i)
#     conn.upsertEdge(h_type, h_id, replaced, t_type, t_id)
#     i+=1

dict_compounds= {'Compound::DB00755': -0.0041017914, 'Compound::DB11094': -0.004272136, 'Compound::DB09341': -0.004339902, 'Compound::DB04868': -0.004389381, 'Compound::DB00815': -0.004389473, 'Compound::DB01222': -0.004392515, 'Compound::DB12291': -0.004671714, 'Compound::DB14681': -0.0046740165, 'Compound::DB00091': -0.0050580334, 'Compound::DB00635': -0.005157881}

disase_list = ['Disease::SARS-CoV2 nsp5']

def topological_link_prediction(disase_list,compound_list):
    cleanead_disase_list = []
    compound_list_cleanead = []
    for d in disase_list:
        d=d.split('::')[1]
        try:
            conn.getVerticesById(vertexType='Disease',vertexIds=d)
        except:
            print(f'The {d} not in cloud yet')
        else:
            cleanead_disase_list.append(d)
            
    for c in compound_list:
        c=c.split('::')[1]
        try:
            conn.getVerticesById(vertexType='Compound',vertexIds=c)
        except:
            print(f'The {c} not in cloud yet')
        else:
            compound_list_cleanead.append(c)
            
    link_prediction_scores = {}
    for d in cleanead_disase_list[:4]:
        for c in compound_list_cleanead[:4]:
            tg_adamic_adar=conn.runInstalledQuery("tg_adamic_adar", {'a':f'{c}','a.type':'Compound','b':f'{d}','b.type':'Disease','e_type':'ALL','print_res':True})
            tg_common_neighbors=conn.runInstalledQuery("tg_common_neighbors", {'a':f'{c}','a.type':'Compound','b':f'{d}','b.type':'Disease','e_type':'ALL','print_res':True})
            tg_preferential_attachment=conn.runInstalledQuery("tg_preferential_attachment", {'a':f'{c}','a.type':'Compound','b':f'{d}','b.type':'Disease','e_type':'ALL','print_res':True})
            tg_total_neighbors=conn.runInstalledQuery("tg_total_neighbors", {'a':f'{c}','a.type':'Compound','b':f'{d}','b.type':'Disease','e_type':'ALL','print_res':True})
            # tg_same_community=conn.runInstalledQuery("tg_same_community", {'a':f'{c}','a.type':'Compound','b':f'{d}','b.type':'Disease','e_type':'ALL','print_res':True})
            tg_resource_allocation=conn.runInstalledQuery("tg_resource_allocation", {'a':f'{c}','a.type':'Compound','b':f'{d}','b.type':'Disease','e_type':'ALL','print_res':True})
            scores={'tg_adamic_adar':tg_adamic_adar[0]['@@sum_closeness'],'tg_common_neighbors':tg_common_neighbors[0]['closeness'],'tg_preferential_attachment':tg_preferential_attachment[0]['closeness'],'tg_total_neighbors':tg_total_neighbors[0]['closeness'],
            'tg_resource_allocation':tg_resource_allocation[0]['@@sum_closeness']}
            link_prediction_scores[f'{d}::{c}'] = scores
    return link_prediction_scores

