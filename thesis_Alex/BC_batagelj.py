import networkx as nx
import networkx.algorithms.thesis_Alex.utils.graphs as g

if __name__ == '__main__':
    G_1 = g.trondheim_graph()

    btwn_g1 = nx.betweenness_centrality(G_1, normalized=False)


