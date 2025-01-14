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

    edge_list = [('Eduardo', 'Domingo'), ('Eduardo', 'Carlos'), ('Eduardo', 'Alejandro'), ('Domingo', 'Carlos'),
                 ('Domingo', 'Alejandro'), ('Carlos', 'Alejandro'), ('Alejandro', 'Bob'),
                 ('Bob', 'Mike'), ('Bob', 'Ike'), ('Bob', 'John'), ('Bob', 'Hal'), ('Bob', 'Lanny'), ('Bob', 'Norm'),
                 ('Mike', 'Ike'), ('Ike', 'Gill'), ('Frank', 'Gill'), ('Gill', 'John'), ('Gill', 'Hal'),
                 ('John', 'Hal'), ('John', 'Lanny'), ('John', 'Karl'), ('Lanny', 'Karl'), ('Karl', 'Ozzie'),
                 ('Ozzie', 'Norm'), ('Norm', 'Vern'), ('Norm', 'Paul'), ('Norm', 'Ultrecht'), ('Norm', 'Sam'),
                 ('Vern', 'Ted'), ('Ted', 'Russ'), ('Russ', 'Quint'), ('Russ', 'Ultrecht'), ('Quint', 'Paul'),
                 ('Quint', 'Ultrecht'), ('Ultrecht', 'Sam'), ('Sam', 'Xavier'), ('Sam', 'Wendle'), ('Xavier', 'Wendle')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G


def g_1():
    G = nx.Graph()

    edge_list = [('3', '4'), ('3', '7'), ('4', '8'), ('6', '7'), ('7', '8')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G


def g_2():
    G = nx.Graph()

    edge_list = [('1', '2'), ('1', '3'), ('2', '4'), ('3', '4'), ('4', '5'), ('5', '6'), ('5', '7'), ('5', '8'),
                 ('6', '9'), ('7', '10'), ('8', '10'), ('9', '10'), ('9', '11')]

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


def triangle_complete_double_longated():
    G = nx.Graph()

    edge_list = [('1', '2'), ('1', '3'), ('2', '3'), ('3', '4'), ('4', '5')]

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


def line_length_5():
    G = nx.Graph()

    edge_list = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6')]

    for edge in edge_list:
        G.add_edge(*edge)

    return G
