import networkx as nx
import networkx.algorithms.thesis_Alex.utils as ut
import pprint
if __name__ == '__main__':
    G = nx.read_edgelist("C:/Users/alexannf/networkXsource/Datasets/facebook/0.edges")
    print(G.number_of_edges())
    print(G.number_of_nodes())

    btwn = nx.betweenness_centrality(G)
    btwn_sort = ut.sort_dict(btwn)
    pprint.pprint(btwn_sort, sort_dicts=False)
