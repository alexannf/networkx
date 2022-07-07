import networkx as nx
import random as rd
from time import time
from datetime import datetime
from os.path import dirname, abspath, join

__all__ = [
    "setup",
    "puzis_state_of_the_art_add",
]

dirname = dirname(dirname(dirname(dirname(abspath(__file__)))))


def get_groups(G, group_size, num_groups):
    groups = []
    for i in range(num_groups):
        groups.append(rd.sample(G.nodes, group_size))
    print(groups)
    if num_groups == 1:
        return groups[0]
    return groups


def setup(edge_stream_size, group_size, num_groups, category, dataset):
    filename = join(dirname, 'thesis_Alex\\datasets\\' + category + '\\' + dataset + '.edges')
    G = nx.read_edgelist(filename)
    edge_stream = rd.sample(G.edges, edge_stream_size)
    G.remove_edges_from(edge_stream)
    groups = get_groups(G, group_size, num_groups)
    return G, edge_stream, groups


def puzis_state_of_the_art_add(G, edge_stream, groups, edge_stream_size, group_size, num_groups, category, dataset):
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    filename = join(dirname, 'thesis_Alex\\results\\' + category + '\\' + dataset + '\\' + dt + '.csv')
    file = open(filename, "w")
    file.write("operation = add, graph nodes = {}, graph edges {}, edge stream size = {}, "
               "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                  edge_stream_size, group_size, num_groups))
    cnt = 1
    total_time = 0.0
    for edge in edge_stream:
        G.add_edge(edge[0], edge[1])
        clk_start = time()
        gbc = nx.group_betweenness_centrality(G, groups)
        clk_end = time()
        total_time += clk_end - clk_start
        print(gbc)
        print("total run time {}. iteration: {} \n".format(cnt, total_time))
        file.write("{}, {}\n".format(cnt, total_time))
        cnt += 1
    file.close()
