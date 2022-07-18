from networkx.algorithms.thesis_Alex.puzis_sota_experiments import *
from networkx.algorithms.thesis_Alex.thesis_experiments_gbc import *
from networkx.algorithms.thesis_Alex.setup import setup

if __name__ == '__main__':
    edge_stream_size = 5
    grp_size = 5
    num_grps = 5

    G_add, edge_stream_add, groups_add = setup("add", edge_stream_size, grp_size, num_grps, "facebook", "0")
    G_rem, edge_stream_rem, groups_rem = setup("remove", edge_stream_size, grp_size, num_grps, "facebook", "0")

    puzis_state_of_the_art_add(G_add, edge_stream_add, groups_add, "facebook", "0")
    thesis_add_gbc(G_add, edge_stream_add, groups_add, "facebook", "0", space=False)
    # thesis_add_gbc(G_add, edge_stream_add, groups_add, "facebook", "0", space=True)

    puzis_state_of_the_art_remove(G_rem, edge_stream_rem, groups_rem, "facebook", "0")
    thesis_remove_gbc(G_rem, edge_stream_rem, groups_rem, "facebook", "0", space=False)
    # thesis_remove_gbc(G_rem, edge_stream_rem, groups_rem, "facebook", "0", space=True)


