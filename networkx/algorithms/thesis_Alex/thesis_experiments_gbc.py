import networkx as nx
from time import time
from datetime import datetime
from os.path import dirname, abspath, join
from networkx.algorithms.thesis_Alex.thesis_algo_gbc import dynamic_group_betweenness_gbc
from copy import deepcopy
import tracemalloc

__all__ = [
    "thesis_add_gbc",
    "thesis_remove_gbc",
]

dirname = dirname(dirname(dirname(dirname(abspath(__file__)))))


def thesis_add_gbc(G, edge_stream, groups, category, dataset, space=False):
    G_dyn = deepcopy(G)
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '.csv')
    file = open(filename, "w")
    file.write("thesis gbc, operation = add, graph nodes = {}, graph edges {}, edge stream size = {}, "
               "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                  len(edge_stream), len(groups[0]), len(groups)))
    cnt = 0
    total_time = 0.0
    clk_init_start = time()
    GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(G_dyn, groups, endpoints=True, xtra_data=True)
    clk_init_stop = time()
    clk_init = clk_init_stop - clk_init_start
    print("\nthesis add new:")

    if space:
        for edge in edge_stream:
            cnt += 1
            tracemalloc.start()
            #  returns new graph G_dyn with new edge added
            GBC, G_dyn, D, sigma, Delta = \
                dynamic_group_betweenness_gbc(G_dyn, groups, D, sigma, Delta, edge, "add", normalized=True, endpoints=True)
            mem_size = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print("space peak after {}. iteration: {}".format(cnt, mem_size[1]))
            file.write("{}, {}, space\n".format(cnt, mem_size[1]))
        file.close()
    else:
        for edge in edge_stream:
            cnt += 1
            clk_start = time()
            #  returns new graph G_dyn with new edge added
            GBC, G_dyn, D, sigma, Delta = \
                dynamic_group_betweenness_gbc(G_dyn, groups, D, sigma, Delta, edge, "add", normalized=True,
                                              endpoints=True)
            clk_end = time()
            total_time += clk_end - clk_start
            if cnt == 1:
                total_time += clk_init
            print("total run time after {}. iteration: {}".format(cnt, total_time))
            file.write("{}, {}\n".format(cnt, total_time))
        file.close()


def thesis_remove_gbc(G, edge_stream, groups, category, dataset, space=False):
    G_dyn = deepcopy(G)
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '.csv')
    file = open(filename, "w")
    file.write("thesis gbc, operation = remove, graph nodes = {}, graph edges {}, edge stream size = {}, "
               "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                  len(edge_stream), len(groups[0]), len(groups)))
    cnt = 0
    total_time = 0.0
    clk_init_start = time()
    GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(G_dyn, groups, endpoints=True, xtra_data=True)
    clk_init_stop = time()
    clk_init = clk_init_stop - clk_init_start

    print("\nthesis remove new:")
    if space:
        for edge in edge_stream:
            cnt += 1
            tracemalloc.start()
            #  returns new graph G_dyn with new edge removed
            GBC, G_dyn, D, sigma, Delta = \
                dynamic_group_betweenness_gbc(
                    G_dyn, groups, D, sigma, Delta, edge, "remove", normalized=True, endpoints=True)
            mem_size = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print("space peak after {}. iteration: {}".format(cnt, mem_size[1]))
            file.write("{}, {}, space\n".format(cnt, mem_size[1]))
        file.close()
    else:
        for edge in edge_stream:
            cnt += 1
            clk_start = time()
            #  returns new graph G_dyn with new edge removed
            GBC, G_dyn, D, sigma, Delta = \
                dynamic_group_betweenness_gbc(
                    G_dyn, groups, D, sigma, Delta, edge, "remove", normalized=True, endpoints=True)
            clk_end = time()
            total_time += clk_end - clk_start
            if cnt == 1:
                total_time += clk_init
            print("total run time after {}. iteration: {}".format(cnt, total_time))
            file.write("{}, {}\n".format(cnt, total_time))
        file.close()
