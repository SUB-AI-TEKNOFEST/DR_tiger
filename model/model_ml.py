import sys
sys.path.append("..")
from operations import file_operations
import torch
import csv
import torch.nn.functional as fn
import numpy as np

allowed_labels = ['Hetionet::CtD::Compound:Disease','GNBR::T::Compound:Disease']

diseases_list = file_operations.open_file_return_list('diseases_names.csv')
allowed_drug = file_operations.allowed_drug
entity_emb = np.load('./data/embed/DRKG_TransE_l2_entity.npy')
rel_emb = np.load('./data/embed/DRKG_TransE_l2_relation.npy')


def get_compound_list(diseases_list,allowed_labels=allowed_labels):
    entity_name_to_id, entity_id_to_name, relation_name_to_id, allowed_relation_ids, allowed_drug_ids,disease_ids = file_operations.entity_relations(allowed_labels,diseases_list)
    allowed_drug_ids = torch.tensor(allowed_drug_ids).long()
    disease_ids = torch.tensor(disease_ids).long()
    allowed_relation_ids = torch.tensor(allowed_relation_ids)
    allowed_drug_tensors = torch.tensor(entity_emb[allowed_drug_ids])
    allowed_relation_tensors = [torch.tensor(rel_emb[rel]) for rel in allowed_relation_ids]

    threshold= 20
    def score(h, r, t):
        return fn.logsigmoid(threshold - torch.norm(h + r - t, p=2, dim=-1))

    allowed_drug_scores = []
    drug_ids = []
    for relation_tensor in range(len(allowed_relation_tensors)):
        rel_vector = allowed_relation_tensors[relation_tensor]
        for disease_id in disease_ids:
            disease_vector = entity_emb[disease_id]
            drug_score = score(allowed_drug_tensors, rel_vector, disease_vector)
            allowed_drug_scores.append(drug_score)
            drug_ids.append(allowed_drug_ids)
    scores = torch.cat(allowed_drug_scores)
    drug_ids = torch.cat(drug_ids)
    idx = torch.flip(torch.argsort(scores), dims=[0])
    scores = scores[idx].numpy()
    drug_ids = drug_ids[idx].numpy()
    _, unique_indices = np.unique(drug_ids, return_index=True)
    # top 10
    topk_indices = np.sort(unique_indices)[:10]
    proposed_dids = drug_ids[topk_indices]
    proposed_scores = scores[topk_indices]
    dict={}
    for i in range(4):
        drug = int(proposed_dids[i])
        score = proposed_scores[i]
        dict[entity_id_to_name[drug]]= score
    return dict

