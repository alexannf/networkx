import networkx as nx
from os.path import dirname, abspath, join

dirname = dirname(abspath(__file__))


def get_graph_properties(G_in):
    n = G_in.number_of_nodes()
    m = G_in.number_of_edges()
    avg_deg = m * 2 / n
    cc = nx.average_clustering(G_in)
    diam = nx.diameter(G_in)  # very slow
    return n, m, avg_deg, cc, diam


def print_graph_properties(n, m, avg_deg, cc, diam):
    print("number of nodes: {}".format(n))
    print("number of edges: {}".format(m))
    print("average degree: {}".format(avg_deg))
    print("clustering coefficient: {}".format(cc))
    print("diameter: {}".format(diam))


if __name__ == "__main__":

    for i in range(1, 31):
        features_filename = join(dirname, 'datasets/scalability/' + str(i) + '.feat')
        edgelist_filename = join(dirname, 'datasets/scalability/' + str(i) + '.edges')

        power_cluster = nx.powerlaw_cluster_graph(500, i, 0.7)
        nx.write_edgelist(power_cluster, edgelist_filename)
        nodes, edges, deg, CC, diameter = get_graph_properties(power_cluster)

        features_file = open(features_filename, "w")
        features_file.write(" nodes: {} \n edges: {} \n average degree: {} \n clustering coefficient: {} \n "
                            "diameter: {}".format(nodes, edges, deg, CC, diameter))
        features_file.close()
        print_graph_properties(nodes, edges, deg, CC, diameter)
