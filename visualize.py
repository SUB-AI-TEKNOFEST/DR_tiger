from tkinter import NE
import networkx as nx
import pyTigerGraph as tg
import pandas as pd
import matplotlib.pyplot as plt
from pyvis.network import Network

net = Network(notebook=True,height='900px',width='75%',bgcolor="#222222",font_color='white')


secret="ji08rpup1652lum47ojvpuei1ievolum"
host="https://offlabel.i.tgcloud.io"  
graphname="DRKG"
username="tigergraph" 
password="utku123"

graph = tg.TigerGraphConnection(host=host, graphname=graphname)
authToken = graph.getToken(secret=secret)
authToken = authToken[0]

conn = tg.TigerGraphConnection(host=host,graphname=graphname,username=username,password=password,apiToken=authToken)

dict_compounds= {'Compound::DB00755': -0.0041017914, 'Compound::DB11094': -0.004272136, 'Compound::DB09341': -0.004339902, 'Compound::DB04868': -0.004389381, 'Compound::DB00815': -0.004389473, 'Compound::DB01222': -0.004392515, 'Compound::DB12291': -0.004671714, 'Compound::DB14681': -0.0046740165, 'Compound::DB00091': -0.0050580334, 'Compound::DB00635': -0.005157881}

disase_list = ['Disease::SARS-CoV2 nsp5']
compound_list = dict_compounds

def html_saved(disase_list,compound_list):
    cleanead_disase_list = []
    for d in disase_list:
        d=d.split('::')[1]
        try:
            conn.getVerticesById(vertexType='Disease',vertexIds=d)
        except:
            print(f'The {d} not in cloud yet')
        else:
            cleanead_disase_list.append(d)
    compound_list = [item.split('::')[1] for item in compound_list.keys()]
    df_main = pd.DataFrame(columns=['from_type','from_id','to_type','to_id'])
    df_list= [df_main]

    for d in cleanead_disase_list:
        try:
            df = conn.getEdgesDataframe(sourceVertexType='Disease',sourceVertexId=d)
        except Exception as e:
            print(e)
        else:
            df_list.append(df)
    for c in compound_list:
        try:
            df =conn.getEdgesDataframe(sourceVertexType='Compound',sourceVertexId=c)
        except Exception as e:
            print(e)
        else:
            df_list.append(df)
    df_main =pd.concat(df_list)
    from_series= df_main['from_type']+df_main['from_id']
    to_series = df_main['to_type']+df_main['to_id']
    df_saved = pd.DataFrame(columns=['from_id','to_id'])
    df_saved['from_id']=from_series
    df_saved['to_id'] = to_series
    G= nx.from_pandas_edgelist(df_saved,source='from_id',target='to_id')
    net.from_nx(G)
    net.show_buttons(filter_=['physics'])
    net.show("templates/visualization.html")



