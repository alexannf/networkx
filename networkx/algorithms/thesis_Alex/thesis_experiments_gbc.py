import networkx as nx
from time import time
from datetime import datetime
from os.path import dirname, abspath, join
from networkx.algorithms.thesis_Alex.thesis_algo_gbc import dynamic_group_betweenness_gbc
from copy import deepcopy
from memory_profiler import memory_usage

__all__ = [
    "thesis_add_gbc",
    "thesis_add_gbc_2",
    "thesis_remove_gbc",
    "thesis_remove_gbc_2",
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
    if space:
        mem_usage_init, data = memory_usage((nx.group_betweenness_centrality, (G_dyn, groups, True, None, True, True)),
                                            retval=True)
        mem_avg_init = sum(mem_usage_init) / (len(mem_usage_init))
        mem_peak_init = max(mem_usage_init)

        GBC, bc, PB, D, sigma, Delta = data
        print("\nthesis add new:")
        for edge in edge_stream:
            cnt += 1
            mem_usage, data = memory_usage((dynamic_group_betweenness_gbc,
                                            (G_dyn, groups, D, sigma, Delta, edge, "add", True, True)),
                                           retval=True)
            mem_avg = sum(mem_usage) / (len(mem_usage))
            mem_peak = max(mem_usage)
            if cnt == 1:
                mem_avg = (mem_avg + mem_avg_init) / 2
                mem_peak = max(mem_peak_init, mem_peak)
            print("{}. iteration: space average = {}, space peak = {}".format(cnt, mem_avg, mem_peak))
            file.write("{}, {}, {}\n".format(cnt, mem_avg, mem_peak))

            GBC, G_dyn, D, sigma, Delta = data  # graph G_dyn here has new edge added
        file.close()

    else:
        total_time = 0.0
        clk_init_start = time()
        GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(G_dyn, groups, endpoints=True, xtra_data=True)
        clk_init_stop = time()
        clk_init = clk_init_stop - clk_init_start

        print("\nthesis add new:")
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
    if space:
        mem_usage_init, data = memory_usage((nx.group_betweenness_centrality, (G_dyn, groups, True, None, True, True)),
                                            retval=True)
        mem_avg_init = sum(mem_usage_init) / (len(mem_usage_init))
        mem_peak_init = max(mem_usage_init)

        GBC, bc, PB, D, sigma, Delta = data
        print("\nthesis remove new:")
        for edge in edge_stream:
            cnt += 1
            mem_usage, data = memory_usage((dynamic_group_betweenness_gbc,
                                            (G_dyn, groups, D, sigma, Delta, edge, "remove", True, True)),
                                           retval=True)
            mem_avg = sum(mem_usage) / (len(mem_usage))
            mem_peak = max(mem_usage)
            if cnt == 1:
                mem_avg = (mem_avg + mem_avg_init) / 2
                mem_peak = max(mem_peak_init, mem_peak)
            print("{}. iteration: space average = {}, space peak = {}".format(cnt, mem_avg, mem_peak))
            file.write("{}, {}, {}\n".format(cnt, mem_avg, mem_peak))
        file.close()

    else:
        total_time = 0.0
        clk_init_start = time()
        GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(G_dyn, groups, endpoints=True, xtra_data=True)
        clk_init_stop = time()
        clk_init = clk_init_stop - clk_init_start

        print("\nthesis remove new:")
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


# both space and time at the same time
def thesis_add_gbc_2(G, edge_stream, groups, category, dataset):
    G_dyn = deepcopy(G)
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    time_filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '_time.csv')
    space_filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '_space.csv')
    time_file = open(time_filename, "w")
    space_file = open(space_filename, "w")
    time_file.write("thesis gbc 2, operation = add, graph nodes = {}, graph edges {}, edge stream size = {}, "
                    "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                       len(edge_stream), len(groups[0]), len(groups)))
    space_file.write("thesis gbc 2, operation = add, graph nodes = {}, graph edges {}, edge stream size = {}, "
                     "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                        len(edge_stream), len(groups[0]), len(groups)))
    cnt = 0
    total_time = 0.0

    clk_init_start = time()
    mem_usage_init, data = memory_usage((nx.group_betweenness_centrality, (G_dyn, groups, True, None, True, True)),
                                        retval=True)
    clk_init_stop = time()

    clk_init = clk_init_stop - clk_init_start
    mem_avg_init = sum(mem_usage_init) / (len(mem_usage_init))
    mem_peak_init = max(mem_usage_init)

    GBC, bc, PB, D, sigma, Delta = data

    print("\nthesis add new 2:")
    for edge in edge_stream:
        cnt += 1
        clk_start = time()
        mem_usage, data = memory_usage((dynamic_group_betweenness_gbc,
                                        (G_dyn, groups, D, sigma, Delta, edge, "add", True, True)),
                                       retval=True)
        clk_end = time()

        total_time += clk_end - clk_start
        mem_avg = sum(mem_usage) / (len(mem_usage))
        mem_peak = max(mem_usage)
        if cnt == 1:
            total_time += clk_init
            mem_avg = (mem_avg + mem_avg_init) / 2
            mem_peak = max(mem_peak_init, mem_peak)

        print("{}. iteration: total time = {}, space average = {}, space peak = {}"
              .format(cnt, total_time, mem_avg, mem_peak))
        time_file.write("{}, {}\n".format(cnt, total_time))
        space_file.write("{}, {}, {}\n".format(cnt, mem_avg, mem_peak))

        GBC, G_dyn, D, sigma, Delta = data  # graph G_dyn here has new edge added
    time_file.close()
    space_file.close()


# both space and time at the same time
def thesis_remove_gbc_2(G, edge_stream, groups, category, dataset):
    G_dyn = deepcopy(G)
    now = datetime.now()
    dt = now.strftime("%Y_%d_%m_%H_%M_%S")
    time_filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '_time.csv')
    space_filename = join(dirname, 'thesis_Alex/results/' + category + '/' + dataset + '/' + dt + '_space.csv')
    time_file = open(time_filename, "w")
    space_file = open(space_filename, "w")
    time_file.write("thesis gbc 2, operation = remove, graph nodes = {}, graph edges {}, edge stream size = {}, "
                    "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                       len(edge_stream), len(groups[0]), len(groups)))
    space_file.write("thesis gbc 2, operation = remove, graph nodes = {}, graph edges {}, edge stream size = {}, "
                     "groups size = {}, number of groups = {}\n".format(G.number_of_nodes(), G.number_of_edges(),
                                                                        len(edge_stream), len(groups[0]), len(groups)))
    cnt = 0
    total_time = 0.0

    clk_init_start = time()
    mem_usage_init, data = memory_usage((nx.group_betweenness_centrality, (G_dyn, groups, True, None, True, True)),
                                        retval=True)
    clk_init_stop = time()

    clk_init = clk_init_stop - clk_init_start
    mem_avg_init = sum(mem_usage_init) / (len(mem_usage_init))
    mem_peak_init = max(mem_usage_init)

    GBC, bc, PB, D, sigma, Delta = data

    print("\nthesis remove new 2:")
    for edge in edge_stream:
        cnt += 1
        clk_start = time()
        mem_usage, data = memory_usage((dynamic_group_betweenness_gbc,
                                        (G_dyn, groups, D, sigma, Delta, edge, "remove", True, True)),
                                       retval=True)
        clk_end = time()

        total_time += clk_end - clk_start
        mem_avg = sum(mem_usage) / (len(mem_usage))
        mem_peak = max(mem_usage)
        if cnt == 1:
            total_time += clk_init
            mem_avg = (mem_avg + mem_avg_init) / 2
            mem_peak = max(mem_peak_init, mem_peak)

        print("{}. iteration: total time = {}, space average = {}, space peak = {}"
              .format(cnt, total_time, mem_avg, mem_peak))
        time_file.write("{}, {}\n".format(cnt, total_time))
        space_file.write("{}, {}, {}\n".format(cnt, mem_avg, mem_peak))

        GBC, G_dyn, D, sigma, Delta = data  # graph G_dyn here has new edge added
    time_file.close()
    space_file.close()
