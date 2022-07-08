import networkx as nx
from time import time
from datetime import datetime
from os.path import dirname, abspath, join
from networkx.algorithms.thesis_Alex.thesis_algo import dynamic_group_betweenness

__all__ = [
    "thesis_add",
    "thesis_remove",
]

dirname = dirname(dirname(dirname(dirname(abspath(__file__)))))


def thesis_add(G, edge_stream, groups, edge_stream_size, group_size, num_groups, category, dataset):
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '.csv')
    file = open(filename, "w")
    file.write("thesis algo, operation = add, graph nodes = {}, graph edges {}, edge stream size = {}, "
               "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                  edge_stream_size, group_size, num_groups))
    cnt = 1
    total_time = 0.0
    for edge in edge_stream:
        G.add_edge(edge[0], edge[1])
        clk_start = time()
        dynamic_group_betweenness()
        clk_end = time()
        total_time += clk_end - clk_start
        print("total run time after {}. iteration: {}".format(cnt, total_time))
        file.write("{}, {}\n".format(cnt, total_time))
        cnt += 1
    file.close()


def thesis_remove(G, edge_stream, groups, edge_stream_size, group_size, num_groups, category, dataset):
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '.csv')
    file = open(filename, "w")
    file.write("puzis SotA, operation = remove, graph nodes = {}, graph edges {}, edge stream size = {}, "
               "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                  edge_stream_size, group_size, num_groups))
    cnt = 1
    total_time = 0.0
    for edge in edge_stream:
        G.remove_edge(edge[0], edge[1])
        clk_start = time()
        dynamic_group_betweenness()
        clk_end = time()
        total_time += clk_end - clk_start
        print("total run time after {}. iteration: {}".format(cnt, total_time))
        file.write("{}, {}\n".format(cnt, total_time))
        cnt += 1
    file.close()
