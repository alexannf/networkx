import networkx.algorithms.thesis_Alex.utils.graphs as g
import networkx.algorithms.thesis_Alex.utils.utils as u


if __name__ == '__main__':
    edge = ('5', 'F')
    operation = "add"
    G_square = g.trondheim_graph()

    # u.compare_kourtellis_no_print(G_square, edge, operation)
    u.compare_kourtellis_bc(G_square, edge, operation)
    # u.compare_kourtellis_D(G_square, edge, operation)
    # u.compare_kourtellis_SP(G_square, edge, operation)
    # u.compare_kourtellis_Delta(G_square, edge, operation)



