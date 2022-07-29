import networkx as nx
import networkx.algorithms.thesis_Alex.utils.graphs as g

if __name__ == '__main__':
    G = g.g_2()
    new_edge = ('5', '6')
    operation = "remove"
    G_new, bc, D, SP, Delta = nx.kourtellis_dynamic_bc_old(G, new_edge, operation)

