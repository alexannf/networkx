import networkx as nx
import networkx.algorithms.thesis_Alex.utils.graphs as g
import networkx.algorithms.thesis_Alex.utils.utils as u

if __name__ == '__main__':
    G = g.line_length_5()
    groups = [['2', '3'], ['3', '4']]

    bc, D, sigma, delta = nx.betweenness_centrality(G, normalized=False, xtra_data=True)
    gbc, Dg, sigma_g, delta_g = nx.group_betweenness_centrality(G, groups, normalized=False, xtra_data=True)

    print("D bc: {}".format(D))
    print("D gbc: {}".format(Dg))
    print()

    print("sigma bc: {}".format(sigma))
    print("sigma gbc: {}".format(sigma_g))
    print()

    print("delta bc: {}".format(delta))
    print("delta gbc: {}".format(delta_g))
    print()
