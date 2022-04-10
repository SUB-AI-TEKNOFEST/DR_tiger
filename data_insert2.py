import pyTigerGraph as tg
import pandas as pd

secret="ji08rpup1652lum47ojvpuei1ievolum"
host="https://offlabel.i.tgcloud.io"  
graphname="DRKG"
username="tigergraph" 
password="utku123"

graph = tg.TigerGraphConnection(host=host, graphname=graphname)
authToken = graph.getToken(secret=secret)
authToken = authToken[0]

conn=tg.TigerGraphConnection(host=host,graphname=graphname,username=username,password=password,apiToken=authToken)

drkg_file = 'data/drkg.tsv'
df = pd.read_csv(drkg_file, sep="\t")
triplets = df.values.tolist()
print(len(triplets))
print(conn.echo())

rtypes = dict() # edge types per entity-couple
entity_dic = {} # entities organized per type
for triplet in triplets:
    [h,r,t] = triplet
    h_type = h.split("::")[0].replace(" " ,"")
    h_id = str(h.split("::")[1])
    t_type = t.split("::")[0].replace(" " ,"")
    t_id = str(t.split("::")[1])

    # add the type if not present
    if not h_type in entity_dic:
        entity_dic[h_type]={}
    if not t_type in entity_dic:
        entity_dic[t_type] ={}

    # add the edge type per type couple
    type_edge = f"{h_type}::{t_type}"
    if not type_edge in rtypes:
        rtypes[type_edge]=[]
    r = r.replace(" ","").replace(":","").replace("+","").replace(">","").replace("-","")
    if not r in rtypes[type_edge]:
        rtypes[type_edge].append(r)

    # spread entities
    if not h_id in entity_dic[h_type]:
        entity_dic[h_type][h_id] = h
    if not t in entity_dic[t_type]:
        entity_dic[t_type][t_id] = t

# schema = ""
# for entity_type in entity_dic.keys():
#     schema += f"CREATE VERTEX {entity_type} (PRIMARY_ID Id STRING) With primary_id_as_attribute=\"true\"\n"
# for endpoints in rtypes:
#     [source_name, target_name] = endpoints.split("::")
#     for edge_name in rtypes[endpoints]:
#         schema += f"CREATE DIRECTED EDGE {edge_name} (FROM {source_name}, TO {target_name})\n"

#TODO:tek tek çalıştırısak açmak lazım
# print(conn.gsql(f"""use global {schema}"""))

conn.getSchema()
for i in range(5122391,0,-1):
    [h,r,t] = triplets[i]
    h_type = h.split("::")[0].replace(" " ,"")
    h_id = str(h.split("::")[1])
    t_type = t.split("::")[0].replace(" " ,"")
    t_id = str(t.split("::")[1])
    replaced = r.replace(" ","").replace(":","").replace("+","").replace(">","").replace("-","")   
    print(i)
    conn.upsertEdge(h_type, h_id, replaced, t_type, t_id)
    i+=1
# print(schema)