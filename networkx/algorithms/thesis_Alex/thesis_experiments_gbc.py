import networkx as nx
from time import time
from datetime import datetime
from os.path import dirname, abspath, join
from networkx.algorithms.thesis_Alex.thesis_algo_gbc import dynamic_group_betweenness_gbc
from copy import deepcopy

__all__ = [
    "thesis_add_gbc",
    "thesis_remove_gbc",
]

dirname = dirname(dirname(dirname(dirname(abspath(__file__)))))


def thesis_add_gbc(G, edge_stream, groups, edge_stream_size, group_size, num_groups, category, dataset):
    G_dyn = deepcopy(G)
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '.csv')
    file = open(filename, "w")
    file.write("thesis gbc, operation = add, graph nodes = {}, graph edges {}, edge stream size = {}, "
               "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                  edge_stream_size, group_size, num_groups))
    cnt = 1
    total_time = 0.0
    print("\nthesis add new:")
    GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(G_dyn, groups, endpoints=True, xtra_data=True)

    for edge in edge_stream:
        clk_start = time()
        #  returns new graph G_dyn with new edge added
        GBC, G_dyn, D, sigma, Delta = \
            dynamic_group_betweenness_gbc(G_dyn, groups, D, sigma, Delta, edge, "add", normalized=True, endpoints=True)
        clk_end = time()
        total_time += clk_end - clk_start
        print("total run time after {}. iteration: {}".format(cnt, total_time))
        file.write("{}, {}\n".format(cnt, total_time))
        cnt += 1
    file.close()


def thesis_remove_gbc(G, edge_stream, groups, edge_stream_size, group_size, num_groups, category, dataset):
    G_dyn = deepcopy(G)
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '.csv')
    file = open(filename, "w")
    file.write("thesis gbc, operation = remove, graph nodes = {}, graph edges {}, edge stream size = {}, "
               "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                  edge_stream_size, group_size, num_groups))
    cnt = 1
    total_time = 0.0

    GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(G_dyn, groups, endpoints=True, xtra_data=True)
    print("\nthesis remove new:")
    for edge in edge_stream:
        clk_start = time()
        #  returns new graph G_dyn with new edge added
        GBC, G_dyn, PB, D, sigma, Delta = \
            dynamic_group_betweenness_gbc(
                G_dyn, groups, D, sigma, Delta, edge, "remove", normalized=True, endpoints=True)
        clk_end = time()
        total_time += clk_end - clk_start
        print("total run time after {}. iteration: {}".format(cnt, total_time))
        file.write("{}, {}\n".format(cnt, total_time))
        cnt += 1
    file.close()
