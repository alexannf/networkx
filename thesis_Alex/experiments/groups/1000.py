import networkx as nx
from networkx.algorithms.thesis_Alex.puzis_sota_experiments import *
from networkx.algorithms.thesis_Alex.thesis_experiments_gbc import *
from networkx.algorithms.thesis_Alex.setup import *
from os.path import dirname, abspath, join
from copy import deepcopy

thesis_Alex_dir = dirname(dirname(dirname(abspath(__file__))))
groups_dir = dirname(abspath(__file__))

if __name__ == '__main__':
    dataset_file = join(thesis_Alex_dir, 'datasets/synthetic/1000.edges')
    stream = join(groups_dir, '1000/50/50.stream')
    category = "groups"

    G = nx.read_edgelist(dataset_file)
    G_add = deepcopy(G)
    G_edges = nx.read_edgelist(stream)

    edge_stream_add = list(G_edges.edges())
    edge_stream_rem = list(reversed(edge_stream_add))
    G_add.remove_edges_from(edge_stream_add)

    for i in range(11, 21):
        groups = get_groups(G_add, i, i)

        puzis_state_of_the_art_add_2(G_add, edge_stream_add, groups, category, str(i))
        thesis_add_gbc_2(G_add, edge_stream_add, groups, category, str(i))
        puzis_state_of_the_art_remove_2(G, edge_stream_rem, groups, category, str(i))
        thesis_remove_gbc_2(G, edge_stream_rem, groups, category, str(i))
