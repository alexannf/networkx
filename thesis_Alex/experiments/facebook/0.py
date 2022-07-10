from networkx.algorithms.thesis_Alex.puzis_sota_experiments import *
from networkx.algorithms.thesis_Alex.thesis_experiments_old import *
from networkx.algorithms.thesis_Alex.thesis_experiments_gbc import *
from networkx.algorithms.thesis_Alex.setup import setup

if __name__ == '__main__':
    G_add, edge_stream_add, groups_add = setup("add", 5, 5, 5, "facebook", "0")
    G_rem, edge_stream_rem, groups_rem = setup("remove", 5, 5, 5, "facebook", "0")

    puzis_state_of_the_art_add(G_add, edge_stream_add, groups_add, 5, 5, 5, "facebook", "0")
    thesis_add_old(G_add, edge_stream_add, groups_add, 5, 5, 5, "facebook", "0")
    thesis_add_gbc(G_add, edge_stream_add, groups_add, 5, 5, 5, "facebook", "0")

    puzis_state_of_the_art_remove(G_rem, edge_stream_rem, groups_rem, 5, 5, 5, "facebook", "0")
    thesis_remove_old(G_rem, edge_stream_rem, groups_rem, 5, 5, 5, "facebook", "0")
    thesis_remove_gbc(G_rem, edge_stream_rem, groups_rem, 5, 5, 5, "facebook", "0")


