from networkx.algorithms.thesis_Alex.puzis_sota_experiments import *
from networkx.algorithms.thesis_Alex.thesis_experiments_gbc import *
from networkx.algorithms.thesis_Alex.setup import *
from networkx.algorithms.thesis_Alex.data import get_data

if __name__ == '__main__':
    edge_stream_add, groups_add = get_data()  # 10 x 10 groups, edge stream size 2000, facebook 107
    G_ad = setup_2("add", edge_stream_add, "facebook", "107")

    # puzis_state_of_the_art_add(G_add, edge_stream_add, groups_add, "facebook", "107")
    # thesis_add_gbc(G_add, edge_stream_add, groups_add, "facebook", "107", space=False)
    #
    # puzis_state_of_the_art_remove(G_rem, edge_stream_rem, groups_rem, "facebook", "107")
    # thesis_remove_gbc(G_rem, edge_stream_rem, groups_rem, "facebook", "107", space=False)
