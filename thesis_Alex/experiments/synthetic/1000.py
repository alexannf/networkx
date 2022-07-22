from networkx.algorithms.thesis_Alex.puzis_sota_experiments import *
from networkx.algorithms.thesis_Alex.thesis_experiments_gbc import *
from networkx.algorithms.thesis_Alex.setup import *

if __name__ == '__main__':
    G_add, edge_stream_add, groups_add = setup("add", 100, 10, 10, "synthetic", "1000")

    # puzis_state_of_the_art_add(G_add, edge_stream_add, groups_add, "synthetic", "1000", space=False)
    # thesis_add_gbc(G_add, edge_stream_add, groups_add, "synthetic", "1000", space=False)

    puzis_state_of_the_art_add(G_add, edge_stream_add, groups_add, "synthetic", "1000", space=True)
    thesis_add_gbc(G_add, edge_stream_add, groups_add, "synthetic", "1000", space=True)

    # puzis_state_of_the_art_remove(G_rem, edge_stream_rem, groups_rem, "facebook", "107", space=False)
    # thesis_remove_gbc(G_rem, edge_stream_rem, groups_rem, "facebook", "107", space=False)
