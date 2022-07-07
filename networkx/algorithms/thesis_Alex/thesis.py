import networkx as nx
import random as rd
from time import time
import os

dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_groups(G, group_size, num_groups):
    groups = []
    for i in range(num_groups):
        groups.append(rd.sample(G.nodes, group_size))
    print(groups)
    if num_groups == 1:
        return groups[0]
    return groups


def setup(edgelist, edge_stream_size, group_size, num_groups):
    G = nx.read_edgelist(edgelist)
    edge_stream = rd.sample(G.edges, edge_stream_size)
    G.remove_edges_from(edge_stream)
    groups = get_groups(G, group_size, num_groups)
    return G, edge_stream, groups


def puzis_state_of_the_art_add(G, edge_stream, groups):
    filename = os.path.join(dirname, 'thesis_Alex\\results\\facebook\\puzis_add.csv')
    file = open(filename, "w")
    cnt = 1
    for edge in edge_stream:
        G.add_edge(edge[0], edge[1])
        clk_start = time()
        gbc = nx.group_betweenness_centrality(G, groups)
        clk_end = time()
        total_time = clk_end - clk_start
        print(gbc)
        print("total run time {}. iteration: {} \n".format(cnt, total_time))
        file.write("{}, {}\n".format(cnt, total_time))
        cnt += 1
    file.close()


if __name__ == '__main__':
    file_loc = os.path.join(dirname, 'thesis_Alex\\datasets\\facebook\\0.edges')
    G, edge_stream, groups = setup(file_loc, 5, 5, 5)
    puzis_state_of_the_art_add(G, edge_stream, groups)



