from networkx.algorithms.thesis_Alex.puzis_sota_experiments import puzis_state_of_the_art_add
from networkx.algorithms.thesis_Alex.thesis_experiments_old import thesis_add
from networkx.algorithms.thesis_Alex.setup import setup

if __name__ == '__main__':
    G, edge_stream, groups = setup("add", 10, 10, 10, "facebook", "107")
    puzis_state_of_the_art_add(G, edge_stream, groups, 10, 10, 10, "facebook", "107")
    thesis_add(G, edge_stream, groups, 10, 10, 10, "facebook", "107")
