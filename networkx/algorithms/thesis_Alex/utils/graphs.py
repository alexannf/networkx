import networkx as nx


def trondheim_graph():
    G = nx.Graph()

    edge_list = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('D', 'E'), ('D', '1'), ('E', 'F'), ('E', 'G'),
                 ('F', 'I'), ('G', 'H'), ('G', 'I'), ('I', 'J'), ('I', 'K'), ('K', 'L'), ('L', 'M'),
                 ('M', '13'), ('L', 'N'), ('N', 'O'), ('O', 'P'), ('P', 'Q'), ('P', 'R'), ('Q', '12'),
                 ('R', '11'), ('1', '2'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '7'), ('4', '5'),
                 ('4', '8'), ('5', '12'), ('6', '7'), ('6', '9'), ('6', 'S'), ('7', '8'), ('7', '9'),
                 ('8', '10'), ('9', '10'), ('10', '11'), ('11', '12'), ('12', '13')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G


def strike_group_social():
    G = nx.Graph()

    edge_list = [('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4'), ('4', '5'),
                 ('5', '6'), ('5', '7'), ('5', '10'), ('5', '11'), ('5', '12'), ('5', '15'), ('6', '7'), ('7', '9'), ('8', '9'),
                 ('9', '10'), ('9', '11'), ('10', '11'), ('10', '12'), ('10', '13'), ('12', '13'), ('13', '14'),
                 ('14', '15'), ('15', '16'), ('15', '20'), ('15', '21'), ('15', '22'), ('16', '17'), ('17', '18'), ('18', '19'),
                 ('18', '21'), ('19', '20'), ('19', '21'), ('21', '22'), ('22', '23'), ('22', '24'), ('23', '24')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G


def g_1():
    G = nx.Graph()

    edge_list = [('3', '4'), ('3', '7'), ('4', '8'), ('6', '7'), ('7', '8')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G


def single_edge_graph():
    G = nx.Graph()
    G.add_edge('1', '2')

    return G


def triangle_longated():
    G = nx.Graph()

    edge_list = [('1', '2'), ('1', '3'), ('3', '4')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G


def triangle_double_longated():
    G = nx.Graph()

    edge_list = [('1', '2'), ('1', '3'), ('3', '4'), ('4', '5')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G

def square_longated():
    G = nx.Graph()

    edge_list = [('1', '2'), ('1', '4'), ('2', '3'), ('3', '5')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G


def incomplete_square():
    G = nx.Graph()

    edge_list = [('1', '2'), ('1', '4'), ('2', '3')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G


def incomplete_triangle():
    G = nx.Graph()

    edge_list = [('1', '2'), ('1', '3')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G

def complete_square():
    G = nx.Graph()

    edge_list = [('1', '2'), ('1', '4'), ('2', '3'), ('3', '4')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G