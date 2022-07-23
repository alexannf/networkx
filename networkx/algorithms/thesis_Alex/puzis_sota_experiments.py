import networkx as nx
from time import time
from datetime import datetime
from os.path import dirname, abspath, join
from copy import deepcopy
from memory_profiler import memory_usage

__all__ = [
    "puzis_state_of_the_art_add",
    "puzis_state_of_the_art_remove",
]

dirname = dirname(dirname(dirname(dirname(abspath(__file__)))))


def puzis_state_of_the_art_add(G, edge_stream, groups, category, dataset, space=False):
    G_dyn = deepcopy(G)
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '.csv')
    file = open(filename, "w")
    file.write("puzis SotA, operation = add, graph nodes = {}, graph edges {}, edge stream size = {}, "
               "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                  len(edge_stream), len(groups[0]), len(groups)))
    cnt = 1
    total_time = 0.0
    print("\npuzis SotA add:")
    if space:
        for edge in edge_stream:
            G_dyn.add_edge(edge[0], edge[1])
            mem_usage = memory_usage(nx.group_betweenness_centrality(G_dyn, groups))
            mem_peak = max(mem_usage)
            print("space peak after {}. iteration: {}".format(cnt, mem_peak))
            file.write("{}, {}, space\n".format(cnt, mem_peak))
            cnt += 1
        file.close()
    else:
        for edge in edge_stream:
            G_dyn.add_edge(edge[0], edge[1])
            clk_start = time()
            nx.group_betweenness_centrality(G_dyn, groups)
            clk_end = time()
            total_time += clk_end - clk_start
            print("total run time after {}. iteration: {}".format(cnt, total_time))
            file.write("{}, {}\n".format(cnt, total_time))
            cnt += 1
        file.close()


def puzis_state_of_the_art_remove(G, edge_stream, groups, category, dataset, space=False):
    G_dyn = deepcopy(G)
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '.csv')
    file = open(filename, "w")
    file.write("puzis SotA, operation = remove, graph nodes = {}, graph edges {}, edge stream size = {}, "
               "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                  len(edge_stream), len(groups[0]), len(groups)))
    cnt = 1
    total_time = 0.0
    print("\npuzis SotA remove:")

    if space:
        for edge in edge_stream:
            G_dyn.remove_edge(edge[0], edge[1])
            mem_usage = memory_usage(nx.group_betweenness_centrality(G_dyn, groups))
            mem_peak = max(mem_usage)
            print("space peak after {}. iteration: {}".format(cnt, mem_peak))
            file.write("{}, {}, space\n".format(cnt, mem_peak))
            cnt += 1
        file.close()
    else:
        for edge in edge_stream:
            G_dyn.remove_edge(edge[0], edge[1])
            clk_start = time()
            nx.group_betweenness_centrality(G_dyn, groups)
            clk_end = time()
            total_time += clk_end - clk_start
            print("total run time after {}. iteration: {}".format(cnt, total_time))
            file.write("{}, {}\n".format(cnt, total_time))
            cnt += 1
    file.close()
