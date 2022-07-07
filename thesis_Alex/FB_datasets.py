import networkx as nx

if __name__ == '__main__':
    d_set_ids = ["0", "107", "348", "414", "686", "698", "1912", "3437", "3980"]

    for d_id in d_set_ids:
        FB = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/" + d_id + ".edges")
        print("nodes for facebook" + d_id + ": {}".format(FB.number_of_nodes()))
        print("edges for facebook" + d_id + ": {}\n".format(FB.number_of_edges()))






