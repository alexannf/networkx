import networkx as nx
from networkx.algorithms.thesis_Alex.puzis_sota_experiments import *
from networkx.algorithms.thesis_Alex.thesis_experiments_gbc import *
from networkx.algorithms.thesis_Alex.setup import *
from os.path import dirname, abspath, join
from copy import deepcopy

thesis_Alex_dir = dirname(dirname(dirname(abspath(__file__))))
friends_dir = dirname(abspath(__file__))

if __name__ == '__main__':
    edge_stream_file = join(friends_dir, '200/2022_27_07_10_13_22.stream')
    dataset_file = join(thesis_Alex_dir, 'datasets/friend/friend.edges')
    G_rem = nx.read_edgelist(dataset_file)
    G_edges = nx.read_edgelist(edge_stream_file)
    edge_stream = list(G_edges.edges())
    edge_stream_rem = list(reversed(edge_stream))

    groups_rem = [['1227', '1546', '2547', '1002', '2185', '475', '289', '290', '1392', '1034'],
                  ['2941', '2570', '2501', '1845', '970', '2006', '2066', '939', '1048', '2464'],
                  ['2861', '2938', '1382', '669', '2519', '1122', '2412', '986', '300', '1149'],
                  ['1537', '746', '5', '2069', '777', '1316', '120', '2917', '2427', '1416'],
                  ['980', '18', '1410', '516', '2498', '195', '1184', '1574', '2390', '671'],
                  ['690', '1342', '2903', '1663', '2733', '91', '1216', '1248', '317', '1027'],
                  ['1021', '57', '1261', '818', '2887', '1351', '390', '79', '944', '332'],
                  ['726', '1414', '771', '622', '276', '2570', '1069', '115', '736', '2691'],
                  ['672', '387', '86', '2579', '947', '793', '1190', '41', '1700', '1562'],
                  ['2702', '691', '255', '7', '1556', '2525', '84', '1562', '1576', '197']]

    category = "friend"
    dataset = "friend"
    # edg_strm_siz = 200

    # G_add, _, _ = setup("add", edg_strm_siz, grp_siz, nm_grps, category, dataset)
    # G_rem = setup_2("remove", edge_stream_add, category, dataset)
    # edge_stream_rem, groups_rem = list(reversed(edge_stream_add)), groups_add
    #
    # puzis_state_of_the_art_add_2(G_add, edge_stream_add, groups_add, category, dataset)
    # thesis_add_gbc_2(G_add, edge_stream_add, groups_add, category, dataset)
    puzis_state_of_the_art_remove_2(G_rem, edge_stream_rem, groups_rem, category, dataset)
    thesis_remove_gbc_2(G_rem, edge_stream_rem, groups_rem, category, dataset)
