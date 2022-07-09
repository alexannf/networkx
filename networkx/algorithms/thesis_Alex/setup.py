import networkx as nx
import random as rd
from os.path import dirname, abspath, join

dirname = dirname(dirname(dirname(dirname(abspath(__file__)))))

__all__ = [
    "setup",
    "get_groups",
]

def get_groups(G, group_size, num_groups):
    groups = []
    for i in range(num_groups):
        groups.append(rd.sample(G.nodes, group_size))
    print("groups:")
    for group in groups:
        print(group)
    if num_groups == 1:
        return groups[0]
    return groups


def setup(operation, edge_stream_size, group_size, num_groups, category, dataset):
    if not (operation == "add" or operation == "remove"):
        raise TypeError("edge operation must be add or remove")

    filename = join(dirname, 'thesis_Alex/datasets/' + category + '/' + dataset + '.edges')
    G = nx.read_edgelist(filename)
    edge_stream = rd.sample(G.edges, edge_stream_size)
    if operation == "add":
        G.remove_edges_from(edge_stream)
    groups = get_groups(G, group_size, num_groups)
    return G, edge_stream, groups
