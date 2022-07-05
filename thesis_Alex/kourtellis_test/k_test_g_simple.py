import networkx.algorithms.thesis_Alex.utils.graphs as g
import networkx.algorithms.thesis_Alex.utils.utils as u


if __name__ == '__main__':
    edge = ('6', '7')
    operation = "add"
    G_square = g.line_length_5()

    # u.compare_kourtellis_no_print(G_square, edge, operation)
    # u.compare_kourtellis_bc(G_square, edge, operation)
    # u.compare_kourtellis_D(G_square, edge, operation)
    # u.compare_kourtellis_SP(G_square, edge, operation)
    # u.compare_kourtellis_Delta(G_square, edge, operation)

    u.side_side_compare_kourtellis_bc(G_square, edge, operation)
    u.side_side_compare_kourtellis_bc(G_square, edge, operation, diff=True)
    u.side_side_compare_kourtellis_D(G_square, edge, operation)
    u.side_side_compare_kourtellis_SP(G_square, edge, operation)
    u.side_side_compare_kourtellis_delta(G_square, edge, operation)



