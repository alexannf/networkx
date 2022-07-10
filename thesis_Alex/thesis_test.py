import networkx as nx
import networkx.algorithms.thesis_Alex.utils.graphs as g
import networkx.algorithms.thesis_Alex.utils.utils as u
from networkx.algorithms.thesis_Alex.thesis_algo_old import dynamic_group_betweenness_old
from copy import deepcopy

if __name__ == '__main__':
    G = g.complete_square()
    G_dyn = g.incomplete_square()
    groups = ['1', '2']

    GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(
        G, groups, normalized=False, endpoints=True, xtra_data=True)

    GBC_in, bc_in, PB_in, D_in, sigma_in, Delta_in = nx.group_betweenness_centrality(
        G_dyn, groups, normalized=False, endpoints=True, xtra_data=True)

    GBC_cop, bc_cop, PB_cop = deepcopy(GBC_in), deepcopy(bc_in), deepcopy(PB_in)
    D_cop, sigma_cop, Delta_cop = deepcopy(D_in), deepcopy(sigma_in), deepcopy(Delta_in)

    GBC_new, G_new, bc_new, PB_new, D_new, sigma_new, Delta_new = \
        dynamic_group_betweenness_old(
            G_dyn, groups, bc_cop, D_cop, sigma_cop, Delta_cop, ('3', '4'), "add", normalized=False, endpoints=True)

    for v in G:
        print("v = {}, Delta_in = {}".format(v, dict(sorted(Delta_in[v].items()))))
        print("v = {}, Delta_new = {}".format(v, dict(sorted(Delta_new[v].items()))))
        print("v = {}, Delta = {}\n".format(v, dict(sorted(Delta[v].items()))))
