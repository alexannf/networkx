import networkx.algorithms.thesis_Alex.utils.graphs as g
import networkx.algorithms.thesis_Alex.utils.utils as u
import networkx as nx
if __name__ == '__main__':
    new_edge = ('3', 'M')
    operation = "add"
    G_square = g.trondheim_graph()

    # u.compare_kourtellis_no_print(G_square, new_edge, operation)
    u.compare_kourtellis_bc(G_square, new_edge, operation)
    # u.compare_kourtellis_D(G_square, new_edge, operation)
    # u.compare_kourtellis_SP(G_square, new_edge, operation)
    # u.compare_kourtellis_Delta(G_square, new_edge, operation)



