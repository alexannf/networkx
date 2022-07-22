import networkx as nx
import random as rd
from datetime import datetime
from os.path import dirname, abspath, join

dirname = dirname(dirname(dirname(dirname(abspath(__file__)))))

__all__ = [
    "setup",
    "setup_2",
    "get_groups",
]


def get_groups(G, group_size, num_groups):
    groups = []
    for i in range(num_groups):
        groups.append(rd.sample(G.nodes, group_size))
    print("\ngroups:")
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

    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")

    edgestream_filename = join(dirname, 'thesis_Alex/experiments/' + category + '/' + dataset +
                               '/' + str(edge_stream_size) + '/' + dt + '.stream')
    groups_filename = join(dirname, 'thesis_Alex/experiments/' + category + '/' + dataset +
                           '/' + str(edge_stream_size) + '/' + dt + '.groups')

    G_temp = nx.Graph()
    G_temp.add_edges_from(edge_stream)
    nx.write_edgelist(G_temp, edgestream_filename)

    groups_file = open(groups_filename, "w")
    for group in groups:
        group_string = ' '.join(group) + '\n'
        groups_file.write(group_string)
    groups_file.close()

    return G, edge_stream, groups


def setup_2(operation, edge_stream, category, dataset):
    if not (operation == "add" or operation == "remove"):
        raise TypeError("edge operation must be add or remove")

    filename = join(dirname, 'thesis_Alex/datasets/' + category + '/' + dataset + '.edges')
    G = nx.read_edgelist(filename)
    if operation == "add":
        G.remove_edges_from(edge_stream)
    return G
