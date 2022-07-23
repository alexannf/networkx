from networkx.algorithms.thesis_Alex.puzis_sota_experiments import *
from networkx.algorithms.thesis_Alex.thesis_experiments_gbc import *
from networkx.algorithms.thesis_Alex.setup import *

if __name__ == '__main__':
    category = "synthetic"
    dataset = "100"
    edg_strm_siz = 20
    grp_siz = 5
    nm_grps = 5

    G_add, edge_stream_add, groups_add = setup("add", edg_strm_siz, grp_siz, nm_grps, category, dataset)
    G_rem = setup_2("remove", edge_stream_add, category, dataset)
    edge_stream_rem, groups_rem = list(reversed(edge_stream_add)), groups_add

    # puzis_state_of_the_art_add(G_add, edge_stream_add, groups_add, category, dataset, space=False)
    # thesis_add_gbc(G_add, edge_stream_add, groups_add, category, dataset, space=False)

    puzis_state_of_the_art_add(G_add, edge_stream_add, groups_add, category, dataset, space=True)
    thesis_add_gbc(G_add, edge_stream_add, groups_add, category, dataset, space=True)

    # puzis_state_of_the_art_remove(G_rem, edge_stream_rem, groups_rem, category, dataset, space=False)
    # thesis_remove_gbc(G_rem, edge_stream_rem, groups_rem, category, dataset, space=False)

    puzis_state_of_the_art_remove(G_rem, edge_stream_rem, groups_rem, category, dataset, space=True)
    thesis_remove_gbc(G_rem, edge_stream_rem, groups_rem, category, dataset, space=True)
