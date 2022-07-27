import networkx as nx
import pprint
import networkx.algorithms.thesis_Alex.utils.graphs as g
import networkx.algorithms.thesis_Alex.utils.utils as u


def generate_node_pairs():
    lttr_comb = []
    for i in range(ord('A'),ord('S')+1):
        for j in range(ord('B'),ord('S')+1):
            if j > i:
                lttr_comb.append([chr(i),chr(j)])
        for k in range(1,14):
            lttr_comb.append([chr(i), "{}".format(k)])
    for a in range(1,14):
        for b in range(2,14):
            if b > a:
                lttr_comb.append(["{}".format(a), "{}".format(b)])
    return lttr_comb


def scores_to_dict(lttr_comb, grp_btwn_cntr_all_pairs):
    dictionary = {}
    for l_comb, grp_btwn in zip(lttr_comb, grp_btwn_cntr_all_pairs):
        dictionary["{}".format(l_comb)] = grp_btwn
    return dictionary


if __name__ == '__main__':
    G = g.trondheim_graph()

    # btwn_centr = nx.algorithms.betweenness_centrality(G, normalized=False)
    # btwn_centr_sorted = sort_dict(btwn_centr)
    # pprint.pprint(btwn_centr_sorted, sort_dicts=False)
    #
    # lttr_comb = generate_node_pairs()
    # grp_btwn_cntr_all_pairs = nx.algorithms.group_betweenness_centrality(G, lttr_comb, normalized=False)
    #
    # grp_btwn_dict = scores_to_dict(lttr_comb, grp_btwn_cntr_all_pairs)
    # grp_btwn_sorted = u.sort_dict(grp_btwn_dict)
    # pprint.pprint(grp_btwn_sorted, sort_dicts=False)

    GBC_control = nx.group_betweenness_centrality(G, [['D', '12'], ['D', 'L'], ['L', '2']], normalized=False)
    print("\n -----------------------------\n{}".format(GBC_control))



