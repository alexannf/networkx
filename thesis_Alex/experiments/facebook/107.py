from networkx.algorithms.thesis_Alex.thesis import setup, puzis_state_of_the_art_add

if __name__ == '__main__':
    G, edge_stream, groups = setup(3000, 20, 20, "facebook", "107")
    puzis_state_of_the_art_add(G, edge_stream, groups, 3000, 20, 20, "facebook", "107")
