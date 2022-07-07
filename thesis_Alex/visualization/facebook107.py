import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    G = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/107.edges")
    nx.draw(G)
    plt.show()