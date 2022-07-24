from networkx.algorithms.thesis_Alex.puzis_sota_experiments import *
from networkx.algorithms.thesis_Alex.thesis_experiments_gbc import *
from networkx.algorithms.thesis_Alex.setup import *

if __name__ == '__main__':
    category = "synthetic"
    dataset = "10000"
    edg_strm_siz = 100
    grp_siz = 10
    nm_grps = 10

    G_add, edge_stream_add, groups_add = setup("add", edg_strm_siz, grp_siz, nm_grps, category, dataset)
    G_rem = setup_2("remove", edge_stream_add, category, dataset)
    edge_stream_rem, groups_rem = list(reversed(edge_stream_add)), groups_add

    puzis_state_of_the_art_add(G_add, edge_stream_add, groups_add, category, dataset)
    thesis_add_gbc(G_add, edge_stream_add, groups_add, category, dataset)

    puzis_state_of_the_art_add(G_add, edge_stream_add, groups_add, category, dataset, space=True)
    thesis_add_gbc(G_add, edge_stream_add, groups_add, category, dataset, space=True)

    puzis_state_of_the_art_remove(G_rem, edge_stream_rem, groups_rem, category, dataset)
    thesis_remove_gbc(G_rem, edge_stream_rem, groups_rem, category, dataset)

    puzis_state_of_the_art_remove(G_rem, edge_stream_rem, groups_rem, category, dataset, space=True)
    thesis_remove_gbc(G_rem, edge_stream_rem, groups_rem, category, dataset, space=True)
