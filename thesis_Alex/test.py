import networkx as nx

if __name__ == '__main__':
    G = nx.read_edgelist("C:/Users/alex/NetworkX/networkx/thesis_Alex/datasets/synthetic/3000.edges")
    print(G.number_of_nodes())
    print(G.number_of_edges())
