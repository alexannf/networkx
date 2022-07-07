from networkx.algorithms.thesis_Alex.thesis import setup, puzis_state_of_the_art_add

if __name__ == '__main__':
    G, edge_stream, groups = setup(5, 5, 5, "facebook", "0")
    puzis_state_of_the_art_add(G, edge_stream, groups, 5, 5, 5, "facebook", "0")
