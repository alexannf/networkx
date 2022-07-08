import networkx as nx


__all__ = [
    "dynamic_group_betweenness",
]


def dynamic_group_betweenness(G, C, D, SP, Delta, edge, operation, normalized=True, endpoints=False):
    GBC = []  # initialize betweenness
    list_of_groups = True
    #  check weather C contains one or many groups
    if any(el in G for el in C):
        C = [C]
        list_of_groups = False
    set_v = {node for group in C for node in group}
    if set_v - G.nodes:  # element(s) of C not in G
        raise nx.NodeNotFound(f"The node(s) {set_v - G.nodes} are in C but not in G.")
