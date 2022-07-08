from networkx.algorithms.thesis_Alex.puzis_sota_experiments import puzis_state_of_the_art_add
from networkx.algorithms.thesis_Alex.setup import setup

if __name__ == '__main__':
    G, edge_stream, groups = setup("add", 5, 5, 5, "facebook", "0")
    puzis_state_of_the_art_add(G, edge_stream, groups, 5, 5, 5, "facebook", "0")
