from networkx.algorithms.thesis_Alex.puzis_sota_experiments import *
from networkx.algorithms.thesis_Alex.thesis_experiments_gbc import *
from networkx.algorithms.thesis_Alex.setup import *

if __name__ == '__main__':
    category = "scalability"
    edg_strm_siz = 50
    grp_siz = 5
    nm_grps = 5

    for i in range(20, 31):
        G_add, edge_stream_add, groups_add = setup("add", edg_strm_siz, grp_siz, nm_grps, category, str(i))
        G_rem = setup_2("remove", edge_stream_add, category, str(i))
        edge_stream_rem, groups_rem = list(reversed(edge_stream_add)), groups_add

        puzis_state_of_the_art_add_2(G_add, edge_stream_add, groups_add, category, str(i))
        thesis_add_gbc_2(G_add, edge_stream_add, groups_add, category, str(i))
        puzis_state_of_the_art_remove_2(G_rem, edge_stream_rem, groups_rem, category, str(i))
        thesis_remove_gbc_2(G_rem, edge_stream_rem, groups_rem, category, str(i))
