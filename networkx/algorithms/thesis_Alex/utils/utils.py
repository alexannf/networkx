import copy

import networkx as nx

__all__ = [
    "compare_kourtellis_bc",
    "compare_kourtellis_D",
    "compare_kourtellis_SP",
    "compare_kourtellis_Delta",
    "compare_kourtellis_no_print",
    "sort_dict",
    "sort_ddict",
    "pretty_print",
]


def compare_kourtellis_bc(G, edge, operation, old=False):
    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])
    else:
        G_new.remove_edge(edge[0], edge[1])

    if old:
        bc1 = nx.betweenness_centrality(G, normalized=False)
        print("bc1: {}\n".format(bc1))

    bc2 = nx.betweenness_centrality(G_new, normalized=False)
    print("bc2: {}\n".format(bc2))

    G_dyn, bc3, D, SP, Delta = nx.kourtellis_dynamic_bc(G, edge, operation)
    print("bc3: {}\n\n".format(bc3))


def compare_kourtellis_D(G, edge, operation, old=False):
    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])
    else:
        G_new.remove_edge(edge[0], edge[1])

    if old:
        bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, normalized=False, xtra_data=True)
        print("D1:")
        pretty_print(D1)

    bc2, D2, SP2, Delta2 = nx.betweenness_centrality(G_new, normalized=False, xtra_data=True)
    print("D2:")
    pretty_print(D2)

    G_dyn, bc3, D3, SP3, Delta3 = nx.kourtellis_dynamic_bc(G, edge, operation)
    print("D3:")
    pretty_print(D3)


def compare_kourtellis_SP(G, edge, operation, old=False):
    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])
    else:
        G_new.remove_edge(edge[0], edge[1])

    if old:
        bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, normalized=False, xtra_data=True)
        print("SP1:")
        pretty_print(SP1)

    bc2, D2, SP2, Delta2 = nx.betweenness_centrality(G_new, normalized=False, xtra_data=True)
    print("SP2:")
    pretty_print(SP2)

    G_dyn, bc3, D3, SP3, Delta3 = nx.kourtellis_dynamic_bc(G, edge, operation)
    print("SP3:")
    pretty_print(SP3)


def compare_kourtellis_Delta(G, edge, operation, old=False):
    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])
    else:
        G_new.remove_edge(edge[0], edge[1])

    if old:
        bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, normalized=False, xtra_data=True)
        print("Delta 1:")
        pretty_print(Delta1)

    bc2, D2, SP2, Delta2 = nx.betweenness_centrality(G_new, normalized=False, xtra_data=True)
    print("Delta 2:")
    pretty_print(Delta2)

    G_dyn, bc3, D3, SP3, Delta3 = nx.kourtellis_dynamic_bc(G, edge, operation)
    print("Delta 3:")
    pretty_print(Delta3)


def compare_kourtellis_no_print(G, edge, operation, old=False):
    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])
    else:
        G_new.remove_edge(edge[0], edge[1])

    if old:
        bc1 = nx.betweenness_centrality(G, normalized=False)

    bc2 = nx.betweenness_centrality(G_new, normalized=False)

    G_dyn, bc3, D, SP, Delta = nx.kourtellis_dynamic_bc(G, edge, operation)


def side_side_compare_kourtellis_bc(G, edge, operation, old=False, diff=False):
    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])
    else:
        G_new.remove_edge(edge[0], edge[1])

    bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, normalized=False, xtra_data=True)
    bc2, D2, SP2, Delta2 = nx.betweenness_centrality(G_new, normalized=False, xtra_data=True)
    G_dyn, bc3, D3, SP3, Delta3 = nx.kourtellis_dynamic_bc(G, edge, operation)

    print("\n")

    for s in G_dyn:
        if old:
            print("s = {}, bc = {}, {}, {}\n".format(s, bc1[s], bc2[s], bc3[s]))
        elif diff:
            print("s = {}, bc diff = {} \n".format(s, bc2[s] - bc3[s]))
        else:
            print("s = {}, bc = {}, {}\n".format(s, bc2[s], bc3[s]))


def side_side_compare_kourtellis_D(G, edge, operation, old=False):
    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])
    else:
        G_new.remove_edge(edge[0], edge[1])

    bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, normalized=False, xtra_data=True)
    bc2, D2, SP2, Delta2 = nx.betweenness_centrality(G_new, normalized=False, xtra_data=True)
    G_dyn, bc3, D3, SP3, Delta3 = nx.kourtellis_dynamic_bc(G, edge, operation)

    for s in G_dyn:
        if old:
            print("s = {}, D1 = {}".format(s, dict(sorted(D1[s].items()))))
        print("s = {}, D2 = {}".format(s, dict(sorted(D2[s].items()))))
        print("s = {}, D3 = {}\n".format(s, dict(sorted(D3[s].items()))))


def side_side_compare_kourtellis_SP(G, edge, operation, old=False):
    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])
    else:
        G_new.remove_edge(edge[0], edge[1])

    bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, normalized=False, xtra_data=True)
    bc2, D2, SP2, Delta2 = nx.betweenness_centrality(G_new, normalized=False, xtra_data=True)
    G_dyn, bc3, D3, SP3, Delta3 = nx.kourtellis_dynamic_bc(G, edge, operation)

    for s in G_dyn:
        if old:
            print("s = {}, SP1 = {}".format(s, dict(sorted(SP1[s].items()))))
        print("s = {}, SP2 = {}".format(s, dict(sorted(SP2[s].items()))))
        print("s = {}, SP3 = {}\n".format(s, dict(sorted(SP3[s].items()))))


def side_side_compare_kourtellis_delta(G, edge, operation, old=False):
    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])
    else:
        G_new.remove_edge(edge[0], edge[1])

    bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, normalized=False, xtra_data=True)
    bc2, D2, SP2, Delta2 = nx.betweenness_centrality(G_new, normalized=False, xtra_data=True)
    G_dyn, bc3, D3, SP3, Delta3 = nx.kourtellis_dynamic_bc(G, edge, operation)

    for s in G_dyn:
        if old:
            print("s = {}, Delta1 = {}".format(s, dict(sorted(Delta1[s].items()))))
        print("s = {}, Delta2 = {}".format(s, dict(sorted(Delta2[s].items()))))
        print("s = {}, Delta3 = {}\n".format(s, dict(sorted(Delta3[s].items()))))


def sort_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))


def sort_ddict(dict_of_dict):
    return {key: sorted(dict_of_dict[key]) for key in sorted(dict_of_dict)}


def pretty_print(mtrx):
    mtrx_sort = dict(sorted(mtrx.items(), key=lambda item: item[0]))
    for key, values in mtrx_sort.items():
        val_sort = dict(sorted(values.items(), key=lambda item: item[0]))
        print("{}: {}".format(key, val_sort))
    print("------------------------------------------------------------ \n")
