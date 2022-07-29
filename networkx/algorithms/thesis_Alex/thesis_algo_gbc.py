import networkx as nx
from networkx.algorithms.thesis_Alex.kourtellis_gbc import algorithm_1_gbc
from copy import deepcopy


__all__ = [
    "dynamic_group_betweenness_gbc",
]


def dynamic_group_betweenness_gbc(G, C, D, sigma, Delta, edge, operation, normalized=True, endpoints=True):
    GBC = []  # initialize betweenness
    list_of_groups = True
    #  check weather C contains one or many groups
    if any(el in G for el in C):
        C = [C]
        list_of_groups = False
    set_v = {node for group in C for node in group}
    if set_v - G.nodes:  # element(s) of C not in G
        raise nx.NodeNotFound(f"The node(s) {set_v - G.nodes} are in C but not in G.")

    G_new, PB, D_new, sigma_new, Delta_new = \
        _dynamic_preprocessing_gbc(G, set_v, D, sigma, Delta, edge, operation)

    # the algorithm for each group
    for group in C:
        group = set(group)  # set of nodes in group
        # initialize the matrices of the sigma and the PB
        GBC_group = 0
        sigma_m = deepcopy(sigma)
        PB_m = deepcopy(PB)
        sigma_m_v = deepcopy(sigma_m)
        PB_m_v = deepcopy(PB_m)
        for v in group:
            GBC_group += PB_m[v][v]
            for x in group:
                for y in group:
                    dxvy = 0
                    dxyv = 0
                    dvxy = 0
                    if not (
                            sigma_m[x][y] == 0 or sigma_m[x][v] == 0 or sigma_m[v][y] == 0
                    ):
                        if D[x][v] == D[x][y] + D[y][v]:
                            dxyv = sigma_m[x][y] * sigma_m[y][v] / sigma_m[x][v]
                        if D[x][y] == D[x][v] + D[v][y]:
                            dxvy = sigma_m[x][v] * sigma_m[v][y] / sigma_m[x][y]
                        if D[v][y] == D[v][x] + D[x][y]:
                            dvxy = sigma_m[v][x] * sigma[x][y] / sigma[v][y]
                    sigma_m_v[x][y] = sigma_m[x][y] * (1 - dxvy)
                    PB_m_v[x][y] = PB_m[x][y] - PB_m[x][y] * dxvy
                    if y != v:
                        PB_m_v[x][y] -= PB_m[x][v] * dxyv
                    if x != v:
                        PB_m_v[x][y] -= PB_m[v][y] * dvxy
            sigma_m, sigma_m_v = sigma_m_v, sigma_m
            PB_m, PB_m_v = PB_m_v, PB_m

        # endpoints
        v, c = len(G), len(group)
        if not endpoints:
            scale = 0
            # if the graph is connected then subtract the endpoints from
            # the count for all the nodes in the graph. else count how many
            # nodes are connected to the group's nodes and subtract that.
            if nx.is_directed(G):
                if nx.is_strongly_connected(G):
                    scale = c * (2 * v - c - 1)
            elif nx.is_connected(G):
                scale = c * (2 * v - c - 1)
            if scale == 0:
                for group_node1 in group:
                    for node in D[group_node1]:
                        if node != group_node1:
                            if node in group:
                                scale += 1
                            else:
                                scale += 2
            GBC_group -= scale

        # normalized
        if normalized:
            scale = 1 / ((v - c) * (v - c - 1))
            GBC_group *= scale

        GBC_group /= 2
        GBC.append(GBC_group)

    if list_of_groups:
        return GBC, G_new, D_new, sigma_new, Delta_new
    else:
        return GBC[0], G_new, D_new, sigma_new, Delta_new


def _dynamic_preprocessing_gbc(G, set_v, D, sigma, Delta, edge, operation):
    G_new, D_new, sigma_new, Delta_new = algorithm_1_gbc(G, D, sigma, Delta, edge, operation)
    Delta_pre = deepcopy(Delta_new)
    for s in G_new:
        for i in G_new:
            if i not in D_new[s]:
                D_new[s][i], Delta_pre[s][i] = float("inf"), 0
            if s != i and D_new[s][i] != float("inf"):
                Delta_pre[s][i] += 1

    PB = dict.fromkeys(G_new)
    for group_node1 in set_v:
        PB[group_node1] = dict.fromkeys(G_new, 0.0)
        for group_node2 in set_v:
            if D[group_node1][group_node2] == float("inf"):
                continue
            for node in G:
                # if node is connected to the two group nodes than continue
                if D_new[node][group_node2] != float("inf") and D_new[node][group_node1] != float("inf"):
                    if (
                            D_new[node][group_node2]
                            == D_new[node][group_node1] + D_new[group_node1][group_node2]
                    ):
                        if sigma_new[node][group_node2] == 0:
                            sigma_new[node][group_node2] = 1
                        PB[group_node1][group_node2] += (
                                Delta_pre[node][group_node2]
                                * sigma_new[node][group_node1]
                                * sigma_new[group_node1][group_node2]
                                / sigma_new[node][group_node2]
                        )
    return G_new, PB, D_new, sigma_new, Delta_new
