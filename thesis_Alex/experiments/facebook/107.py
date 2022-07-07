from networkx.algorithms.thesis_Alex.thesis import setup, puzis_state_of_the_art_add

if __name__ == '__main__':
    G, edge_stream, groups = setup(5, 5, 5, "facebook", "107")
    puzis_state_of_the_art_add(G, edge_stream, groups, 6749, 20, 20, "facebook", "107")
