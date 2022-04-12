
import torch, os
from torch.utils import data as torch_data
from torchdrug import core, datasets, tasks, models, data, utils
import sys
sys.path.append("..")
	
class DRKG(data.KnowledgeGraphDataset):
    """
    DRKG for knowledge graph reasoning.

    Parameters:
        path (str): path to store the dataset
        verbose (int, optional): output verbose level
    """

    def __init__(self, path, verbose = 1):

        self.load_tsv('drkg.tsv', verbose = verbose)


dataset = DRKG(".data")
lengths = [int(0.8 * len(dataset)), int(0.1 * len(dataset))]
lengths += [len(dataset) - sum(lengths)]
train_set, valid_set, test_set = torch_data.random_split(dataset, lengths)

train_set, valid_set, test_set = torch_data.random_split(dataset, lengths)
print("train: ", len(train_set), "val: ", len(valid_set), "test: ", len(test_set))

model = models.RotatE(num_entity = dataset.num_entity,
                      num_relation = dataset.num_relation,
                      embedding_dim = 2048, max_score = 9)

task = tasks.KnowledgeGraphCompletion(model, num_negative = 256,
                                      adversarial_temperature = 1)

optimizer = torch.optim.Adam(task.parameters(), lr = 2e-5)
solver = core.Engine(task, train_set, valid_set, test_set, optimizer,
                      batch_size = 1024)
solver.train(num_epoch = 5)