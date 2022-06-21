import collections
import math
from collections import deque, defaultdict
import networkx as nx
from networkx.exception import NetworkXUnfeasible
import copy
from enum import Enum
import pprint

__all__ = [
    "kourtellis_dynamic_bc",
]


class State(Enum):
    D = "descending"
    U = "ascending"
    N = "untouched"
    P = "pivot"
    NP = "not a pivot"
    M = "disconnected"


class Operation(Enum):
    A = "add"
    D = "remove"


def kourtellis_dynamic_bc(G, new_edge, operation):
    bc, D, SP, Delta = nx.betweenness_centrality(G, xtra_data=True, normalized=False)

    G_new, bc, D, SP, Delta = algorithm_1(G, bc, D, SP, Delta, new_edge, operation)
    return G_new, bc, D, SP, Delta


def algorithm_1(G, bc, D, SP, Delta, edge, operation):
    if not (operation == "add" or operation == "remove"):
        raise TypeError("edge operation must be add or remove")

    Dd, SPd, Delta_d, flag = {}, {}, {}, {}  # data structures to store updates from dynamic addition/deletion

    G_new = copy.deepcopy(G)
    if operation == "add":
        G_new.add_edge(edge[0], edge[1])  # will add new node(s) to G based on endpoints in new edge
    else:
        if not G.has_edge(edge[0], edge[1]):
            raise NetworkXUnfeasible("edge {} is not in G and cannot be removed".format(edge))
        G_new.remove_edge(edge[0], edge[1])  # island node(s) will still exist in G but not affect computation

    # print("before algo starts, bc[1] = {}, bc[2] = {}".format(bc['1'], bc['2']))

    for s in G_new:
        if s == '10':
            print("investigate")

        u_high, u_low, D, SP = find_lowest_highest(G, s, edge[0], edge[1], D, SP)
        dd = D[s][u_low] - D[s][u_high]  # distance difference between endpoints of newly added edge relative to s

        if dd == 0:
            continue  # same level addition/deletion

        if dd >= 1:
            for r in G:
                Dd[r], SPd[r], Delta_d[r] = D[s][r], SP[s][r], 0  # initialize dynamic data structures
                flag[r] = State.N
            Q_lvl = defaultdict(collections.deque)
            Q_bfs = deque([u_low])  # add the node which is the edge endpoint furthest away from source s

            if operation == "add":
                if dd == 1:  # 0 level rise
                    bc, Dd, SPd, Delta_d, flag = \
                        algorithm_2(G_new, s, u_low, u_high, Q_lvl, Q_bfs,
                                    flag, bc, SP, SPd, Dd, Delta, Delta_d, operation)

                if dd > 1:  # 1 or more level rise
                    bc, Dd, SPd, Delta_d, flag = \
                        algorithm_4(G_new, s, u_low, u_high, Q_lvl, Q_bfs,
                                    flag, bc, SP, SPd, D, Dd, Delta, Delta_d)

            else:
                if has_predecessors(G, s, u_low, u_high, D):  # 0 level drop
                    bc, Dd, SPd, Delta_d, flag = \
                        algorithm_2(G_new, s, u_low, u_high, Q_lvl, Q_bfs,
                                    flag, bc, SP, SPd, Dd, Delta, Delta_d, operation)
                else:  # 1 or more level drop
                    bc, Dd, SPd, Delta_d, flag = \
                        algorithm_6(G_new, s, u_low, u_high, Q_lvl, flag, bc, SP, SPd, D, Dd, Delta, Delta_d)

        for r in G_new:
            SP[s][r], D[s][r] = SPd[r], Dd[r]
            if flag[r] != State.N:
                Delta[s][r] = Delta_d[r]

        print("s = {}, bc[1] = {}, bc[2] = {}".format(s, bc['1'], bc['2']))

        # pretty_print_datastructures(s, bc, D, SP, Delta)

    return G_new, bc, D, SP, Delta


# is run when the distances of the endpoints of an added/deleted edge differ with exactly one (with respect to s)
def algorithm_2(G, s, u_low, u_high, Q_lvl, Q_bfs, flag, bc, SP, SPd, Dd, Delta, Delta_d, operation):
    Q_lvl[Dd[u_low]].append(u_low)
    flag[u_low] = State.D
    if operation == "add":
        SPd[u_low] += SP[s][u_high]
    if operation == "remove":
        SPd[u_low] -= SP[s][u_high]

    while Q_bfs:
        v = Q_bfs.popleft()
        for w in G[v]:  # adjacent nodes
            if Dd[w] == Dd[v] + 1:  # is discovered node 1 step further from the source?
                if flag[w] == State.N:  # if not discovered yet
                    Q_lvl[Dd[w]].append(w)  #
                    flag[w] = State.D
                    Q_bfs.append(w)
                SPd[w] += (SPd[v] - SP[s][v])
    if operation == "remove":
        Delta_d[u_high] = Delta[s][u_high] - (SP[s][u_high]/SP[s][u_low]) * (1 + Delta[s][u_low])
        Q_lvl[Dd[u_high]].append(u_high)
        flag[u_high] = State.U

    level = G.number_of_nodes()
    while level > 0:
        while Q_lvl[level]:
            w = Q_lvl[level].popleft()
            for v in G[w]:  # adjacent nodes
                if Dd[v] < Dd[w]:  # is discovered node closer to the source?
                    flag, Delta_d, Q_lvl, a = algorithm_3(s, v, w, flag, Delta, Delta_d, SP, SPd, Q_lvl, level)
                    if operation == "add":
                        if flag[v] == State.U and (v != u_high or w != u_low):
                            Delta_d[v] -= a  # if undiscovered, subtract the delta contribution from the old G
                    if operation == "remove":
                        if flag[v] == State.U:
                            Delta_d[v] -= a
            if w != s:
                bc[w] += (Delta_d[w] - Delta[s][w])/2
        level -= 1

    return bc, Dd, SPd, Delta_d, flag


# dependency accumulation phase
def algorithm_3(s, v, w, flag, Delta, Delta_d, SP, SPd, Q_lvl, level):
    if flag[v] == State.N:
        flag[v] = State.U
        Delta_d[v] = Delta[s][v]
        Q_lvl[level-1].append(v)
    Delta_d[v] += (SPd[v]/SPd[w]) * (1 + Delta_d[w])
    a = (SP[s][v]/SP[s][w]) * (1 + Delta[s][w])
    return flag, Delta_d, Q_lvl, a


# is run when the distances of the endpoints of an added edge differ with more than one (with respect to s)
def algorithm_4(G, s, u_low, u_high, Q_lvl, Q_bfs, flag, bc, SP, SPd, D, Dd, Delta, Delta_d):
    Dd[u_low] = D[s][u_high] + 1
    Q_lvl[Dd[u_low]].append(u_low)
    while Q_bfs:
        v = Q_bfs.popleft()
        flag[v], SPd[v] = State.D, 0
        for w in G[v]:  # adjacent nodes
            if Dd[w] + 1 == Dd[v]:  # is discovered node 1 step further from the source?
                SPd[v] += SPd[w]

            # is discovered node undiscovered and more than 1 step further from the source?
            if Dd[w] > Dd[v] and flag[w] == State.N:
                flag[w], Dd[w] = State.D, Dd[v] + 1
                Q_lvl[Dd[w]].append(w)
                Q_bfs.append(w)

            # is discovered node equally far away from the source as parent for both the old and new graph?
            if Dd[w] == Dd[v] and D[s][w] != D[s][v]:
                if flag[w] == State.N:
                    flag[w] = State.D
                    Q_lvl[Dd[w]].append(w)
                    Q_bfs.append(w)
    level = G.number_of_nodes()
    while level > 0:
        while Q_lvl[level]:
            w = Q_lvl[level].popleft()
            for v in G[w]:
                if Dd[v] < Dd[w]:  # is discovered node closer to the source?
                    flag, Delta_d, Q_lvl, a = algorithm_3(s, v, w, flag, Delta, Delta_d, SP, SPd, Q_lvl, level)
                    if flag[v] == State.U and (v != u_high or w != u_low):
                        Delta_d[v] -= a

            if w != s:
                bc[w] += (Delta_d[w] - Delta[s][w])/2

        level -= 1

    return bc, Dd, SPd, Delta_d, flag


def algorithm_6(G, s, u_low, u_high, Q_lvl, flag, bc, SP, SPd, D, Dd, Delta, Delta_d):
    PQ, Q_bfs = defaultdict(collections.deque), deque([])
    first = G.number_of_nodes()
    Q_bfs.append(u_low)
    flag[u_low] = State.NP
    while Q_bfs:
        v = Q_bfs.popleft()
        for w in G[v]:  # adjacent nodes
            if D[s][w] + 1 == D[s][v] and flag[w] == State.N and flag[v] != State.P:
                PQ[Dd[v]].append(v)
                flag[v] = State.P  # a new pivot
                if first > D[s][v]:
                    first = D[s][v]  # the first pivot
            elif D[s][w] == D[s][v] + 1 or D[s][w] == D[s][v]:
                if flag[w] == State.N:
                    Q_bfs.append(w)
                    flag[w] = State.NP
    if PQ:
        bc, Dd, SPd, Delta_d, flag = \
            algorithm_7(G, s, u_low, u_high, Q_lvl, flag, bc, SP, SPd, D, Dd, Delta, Delta_d, PQ, first)
        return bc, Dd, SPd, Delta_d, flag
    else:
        bc, Dd, SPd, Delta_d, flag = \
            algorithm_10(G, s, u_low, u_high, Q_lvl, flag, bc, SP, SPd, D, Dd, Delta, Delta_d)
        return bc, Dd, SPd, Delta_d, flag


def algorithm_7(G, s, u_low, u_high, Q_lvl, flag, bc, SP, SPd, D, Dd, Delta, Delta_d, PQ, first):
    Q_bfs = deque([])
    Q_bfs.extend(PQ[first])
    nxt = first + 1
    while Q_bfs:
        v = Q_bfs.popleft()
        flag[v], SPd[v] = State.D, 0
        Q_lvl[Dd[v]].append(v)
        if nxt == Dd[v] + 1:
            Q_bfs.extend(PQ[nxt])
            nxt += 1
        for w in G[v]:  # adjacent nodes
            if flag[w] == State.NP:
                flag[w], Dd[w] = State.D, Dd[v] + 1
                Q_bfs.append(w)
            elif flag[w] == State.P:
                flag[w] = State.D
            else:
                if Dd[w] + 1 == Dd[v]:
                    SPd[v] += SPd[w]
                if Dd[w] == Dd[v] and D[s][w] != D[s][v]:
                    if D[s][w] > D[s][v] and flag[w] != State.D:
                        flag[w] = State.D
                        Q_lvl[Dd[w]].append(w)
                        Q_bfs.append(w)
    Delta_d[u_high] = Delta[s][u_high] - ((SP[s][u_high]/SP[s][u_low]) * (1 + Delta[s][u_low]))
    Q_lvl[Dd[u_high]].append(u_high)
    flag[u_high] = State.U
    level = G.number_of_nodes()
    while level > 0:
        while Q_lvl[level]:
            w = Q_lvl[level].pop()
            if w == '1':
                print("investigate")
            for v in G[w]:
                if Dd[v] < Dd[w]:
                    flag, Delta_d, Q_lvl, a = algorithm_3(s, v, w, flag, Delta, Delta_d, SP, SPd, Q_lvl, level)
                    a = 0
                    if D[s][w] > D[s][v]:
                        a = (SP[s][v]/SP[s][w]) * (1 + Delta[s][w])
                    elif D[s][w] < D[s][v]:
                        a = (SP[s][w] / SP[s][v]) * (1 + Delta[s][v])
                    if flag[v] == State.U:
                        Delta_d[v] -= a
            if w != s:
                if math.isclose(0.0, round(bc[w], 4) + round(((Delta_d[w] - Delta[s][w]) / 2), 4)):
                    bc[w] = 0.0
                else:
                    bc[w] += (Delta_d[w] - Delta[s][w]) / 2
        level -= 1
    return bc, Dd, SPd, Delta_d, flag


def algorithm_10(G, s, u_low, u_high, Q_lvl, flag, bc, SP, SPd, D, Dd, Delta, Delta_d):
    Q_bfs = deque(u_low)
    Dd[u_low], SPd[u_low], Delta_d[u_low] = -1, 0, 0

    while Q_bfs:
        v = Q_bfs.popleft()
        for w in G[v]:  # adjacent nodes
            if D[s][w] == D[s][v] + 1:
                if flag[w] == State.NP:
                    Q_bfs.append(w)
                    flag[w] = State.M
                    Dd[w], SPd[w], Delta_d[w] = -1, 0, 0
                bc[v] -= ((SP[s][v]/SP[s][w]) * (1 + Delta[s][w]))/2

    Delta_d[u_high] = 0
    Q_lvl[Dd[u_high]].append(u_high)
    flag[u_high] = State.U
    level = G.number_of_nodes()
    while level > 0:
        while Q_lvl[level]:
            w = Q_lvl[level].pop()
            for v in G[w]:
                if Dd[v] < Dd[w]:
                    flag, Delta_d, Q_lvl, a = algorithm_3(s, v, w, flag, Delta, Delta_d, SP, SPd, Q_lvl, level)
                    if flag[v] == State.U:
                        Delta_d[v] -= a
            if w != s:
                bc[w] += (Delta_d[w] - Delta[s][w])/2
        level -= 1
    return bc, Dd, SPd, Delta_d, flag


def find_lowest_highest(G, s, u_1, u_2, D, SP):
    if G.has_node(u_1) and G.has_node(u_2):
        if D[s][u_1] < D[s][u_2]:
            return u_1, u_2, D, SP
        else:
            return u_2, u_1, D, SP

    else:
        if G.has_node(u_1):
            D[s][u_2] = D[s][u_1] + 1  # new node added, 1 distance further away than u_1
            SP[s][u_2] = SP[s][u_1]  # new node added, inherits the shortest path from tail of endpoint
            return u_1, u_2, D, SP
        elif G.has_node(u_2):
            D[s][u_1] = D[s][u_2] + 1  # new node added, 1 distance further away than u_2
            SP[s][u_1] = SP[s][u_2]  # new node added, inherits the shortest path from tail of endpoint
            return u_2, u_1, D, SP
        else:
            D[s][u_1], D[s][u_2] = float('inf'), float('inf')  # incoming edge has two new nodes
            SP[s][u_1], SP[s][u_2] = 0, 0
            return u_2, u_1, D, SP


def has_predecessors(G, s, u_low, u_high, D):
    for v in G[u_low]:
        if D[s][v] < D[s][u_low] and v != u_high:
            return True
    return False


def print_datastructures(s, bc=None, D=None, SP=None, Delta=None):
    if bc:
        print("s  = {}, bc = {}".format(s, bc))

    if D:
        print("s  = {}, D[s] = {}".format(s, D[s]))

    if SP:
        print("s  = {}, SP[s] = {}".format(s, SP[s]))

    if Delta:
        print("s  = {}, Delta[s] = {}".format(s, Delta[s]))


def pretty_print_datastructures(s, bc=None, D=None, SP=None, Delta=None):
    if bc:
        print("s  = {}, bc:".format(s))
        pprint.pprint(bc)

    if D:
        print("s  = {}, D[s]:".format(s))
        pprint.pprint([s])

    if SP:
        print("s  = {}, SP[s]:".format(s))
        pprint.pprint(SP[s])

    if Delta:
        print("s  = {}, Delta[s]:".format(s))
        pprint.pprint(Delta[s])
