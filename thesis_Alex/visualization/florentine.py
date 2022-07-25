import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy
from time import sleep

def scores_to_dict(lttr_comb, grp_btwn_cntr_all_pairs):
    dictionary = {}
    for l_comb, grp_btwn in zip(lttr_comb, grp_btwn_cntr_all_pairs):
        dictionary["{}".format(l_comb)] = grp_btwn
    return dictionary


if __name__ == '__main__':
    G = nx.florentine_families_graph()
    G.remove_edge('Guadagni', 'Bischeri')
    # G_dyn = deepcopy(G)
    # G_dyn.remove_node('Medici')
    bc = nx.betweenness_centrality(G, normalized=False)
    #
    # pos = nx.spring_layout(G, seed=15)
    #
    # pos_higher = {}
    # y_off = 0.1  # offset on the y axis
    # x_off = 0.0
    #
    # for k, v in pos.items():
    #     pos_higher[k] = (v[0] + x_off, v[1] + y_off)
    #
    # # nx.draw(G, pos)
    # # nx.draw_networkx_labels(G, pos_higher)
    # # plt.show()
    #
    # nx.draw(G_dyn, pos)
    # nx.draw_networkx_labels(G_dyn, pos_higher)
    # plt.show()

    combs = []
    for name in G.nodes():
        for nm in G.nodes():
            comb1 = [name, nm]
            comb2 = [nm, name]
            if name != nm and comb1 not in combs and comb2 not in combs:
                combs.append(comb1)

    gbc = nx.group_betweenness_centrality(G, combs, normalized=False)

    gbc_pretty = scores_to_dict(combs, gbc[0])
    print(dict(sorted(bc.items(), key=lambda item: item[1], reverse=True)))
    print(dict(sorted(gbc_pretty.items(), key=lambda item: item[1], reverse=True)))
