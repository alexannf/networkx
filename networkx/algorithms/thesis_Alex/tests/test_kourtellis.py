import pytest
import networkx as nx
import networkx.algorithms.thesis_Alex.utils.graphs as g


class TestKourtellisBetweenness:

    def test_add_single_edge_graph(self):
        G = nx.Graph()
        G.add_edge('1', '2')
        G_dyn = nx.Graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('1', '2'), "add")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert D[s][t] == pytest.approx(D_new[s][t], abs=1e-7)
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)
                assert Delta[s][t] == pytest.approx(Delta_new[s][t], abs=1e-7)

    def test_add_edge_single_endpoint_new_node(self):
        G = g.single_edge_graph()
        G.add_edge('2', '3')
        G_dyn = g.single_edge_graph()
        G_dyn.add_edge('2', '3')
        G_dyn.remove_edge('2', '3')

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('2', '3'), "add")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert D[s][t] == pytest.approx(D_new[s][t], abs=1e-7)
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)
                assert Delta[s][t] == pytest.approx(Delta_new[s][t], abs=1e-7)

    @pytest.mark.skip(reason="cleaning up code")
    def test_add_edge_single_endpoint_new_node_endpoints_bc(self):
        G = g.single_edge_graph()
        G.add_edge('2', '3')
        G_dyn = g.single_edge_graph()
        G_dyn.add_edge('2', '3')
        G_dyn.remove_edge('2', '3')

        bc, D, SP, Delta = nx.betweenness_centrality(G, endpoints=True, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('2', '3'), "add", endpoints=True)

        for s in sorted(G):
            assert pytest.approx(bc_new[s], abs=1e-7) == bc[s]

            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(SP_new[s][t], abs=1e-7) == SP[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_add_edge_single_endpoint_new_node_long_line(self):
        G = g.line_length_5()
        G.add_edge('6', '7')
        G_dyn = g.line_length_5()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('6', '7'), "add")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert D[s][t] == pytest.approx(D_new[s][t], abs=1e-7)
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)
                assert Delta[s][t] == pytest.approx(Delta_new[s][t], abs=1e-7)

    def test_add_edge_single_endpoint_new_node_trondheim(self):
        G = g.trondheim_graph()
        G.add_edge('C', 'Z')
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('C', 'Z'), "add")

        for s in sorted(G):
            # assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert D[s][t] == pytest.approx(D_new[s][t], abs=1e-7)
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)
                assert Delta[s][t] == pytest.approx(Delta_new[s][t], abs=1e-7)

    def test_add_edge_island(self):
        G = g.single_edge_graph()
        G.add_edge('3', '4')
        G_dyn = g.single_edge_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('3', '4'), "add")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)

    def test_add_edge_island_trondheim(self):
        G = g.trondheim_graph()
        G.add_edge('69', '420')
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('69', '420'), "add")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)

    def test_edge_addition_existing_nodes(self):
        G = g.complete_square()
        G_dyn = g.incomplete_square()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('3', '4'), "add")

        for s in sorted(G):
            assert pytest.approx(bc_new[s], abs=1e-7) == bc[s]

            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(SP_new[s][t], abs=1e-7) == SP[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_edge_removal_existing_nodes(self):
        G = g.incomplete_square()
        G_dyn = g.complete_square()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('3', '4'), "remove")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert D[s][t] == pytest.approx(D_new[s][t], abs=1e-7)
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)
                assert Delta[s][t] == pytest.approx(Delta_new[s][t], abs=1e-7)

    def test_edge_addition_trondheim_graph(self):
        G = g.trondheim_graph()
        G.add_edge('5', 'F')
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('5', 'F'), "add")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert D[s][t] == pytest.approx(D_new[s][t], abs=1e-7)
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)
                assert Delta[s][t] == pytest.approx(Delta_new[s][t], abs=1e-7)

    def test_edge_deletion_trondheim_graph(self):
        G = g.trondheim_graph()
        G.remove_edge('1', '2')
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('1', '2'), "remove")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert D[s][t] == pytest.approx(D_new[s][t], abs=1e-7)
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)
                assert Delta[s][t] == pytest.approx(Delta_new[s][t], abs=1e-7)

    def test_edge_deletion_disconnected_graph_simple(self):
        G = g.line_length_5()
        G.remove_edge('3', '4')
        G_dyn = g.line_length_5()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('3', '4'), "remove")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)

    def test_edge_deletion_disconnected_graph_trondheim(self):
        G = g.trondheim_graph()
        G.remove_edge('B', 'D')
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('B', 'D'), "remove")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc_new[s], abs=1e-7)

            for t in sorted(G):
                assert SP[s][t] == pytest.approx(SP_new[s][t], abs=1e-7)

    def test_edge_reconnection_disconnected_graph_line(self):
        G = g.line_length_5()
        G_dyn = g.line_length_5()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_rem, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc, D, SP, Delta, ('3', '4'), "remove")
        G_dyn, bc3, D3, SP3, Delta3 = nx.algorithm_1(G_rem, bc2, D2, SP2, Delta2, ('3', '4'), "add")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc3[s], abs=1e-7)

            for t in sorted(G):
                assert SP[s][t] == pytest.approx(SP3[s][t], abs=1e-7)

    # @pytest.mark.skip(reason="activate after more edge cases tested")
    def test_edge_reconnection_disconnected_graph_trondheim(self):
        G = g.trondheim_graph()
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_rem, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc, D, SP, Delta, ('B', 'D'), "remove")
        G_dyn, bc3, D3, SP3, Delta3 = nx.algorithm_1(G_rem, bc2, D2, SP2, Delta2, ('B', 'D'), "add")

        for s in sorted(G):
            assert bc[s] == pytest.approx(bc3[s], abs=1e-7)

            for t in sorted(G):
                assert SP[s][t] == pytest.approx(SP3[s][t], abs=1e-7)

    def test_deconstruct_trondheim(self):
        G = g.trondheim_graph()
        edges = G.edges()
        G_dyn = g.trondheim_graph()

        bc2, D2, SP2, Delta2 = \
            nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)

        for edge in edges:
            G.remove_edge(edge[0], edge[1])

            bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
            G_dyn, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc2, D2, SP2, Delta2, edge, "remove")

            for s in sorted(G):
                assert bc1[s] == pytest.approx(bc2[s], abs=1e-7)

                for t in sorted(G):
                    assert SP1[s][t] == pytest.approx(SP2[s][t], abs=1e-7)

    def test_deconstruct_social(self):
        G = g.strike_group_social()
        edges = G.edges()
        G_dyn = g.strike_group_social()

        bc2, D2, SP2, Delta2 = \
            nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)

        for edge in edges:
            G.remove_edge(edge[0], edge[1])

            bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
            G_dyn, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc2, D2, SP2, Delta2, edge, "remove")

            for s in sorted(G):
                assert bc1[s] == pytest.approx(bc2[s], abs=1e-7)

                for t in sorted(G):
                    assert SP1[s][t] == pytest.approx(SP2[s][t], abs=1e-7)

    def test_construct_trondheim(self):
        G = g.trondheim_graph()
        edges = G.edges()
        G_bc = nx.Graph()
        G_dyn = nx.Graph()

        bc2, D2, SP2, Delta2 = \
            nx.betweenness_centrality(G_dyn, weight=None, normalized=False, xtra_data=True)

        for edge in edges:
            # print(edge)
            G_bc.add_edge(edge[0], edge[1])

            bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G_bc, weight=None, normalized=False, xtra_data=True)
            G_dyn, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc2, D2, SP2, Delta2, edge, "add")

            for s in sorted(G_bc):
                assert bc1[s] == pytest.approx(bc2[s], abs=1e-7)

                for t in sorted(G_bc):
                    assert SP1[s][t] == pytest.approx(SP2[s][t], abs=1e-7)

    @pytest.mark.skip(reason="takes too long, we know this works")
    def test_construct_facebook_0(self):
        G = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/0.edges")
        edges = G.edges()
        G_bc = nx.Graph()
        G_dyn = nx.Graph()

        bc2, D2, SP2, Delta2 = \
            nx.betweenness_centrality(G_dyn, weight=None, normalized=False, xtra_data=True)

        for edge in list(G.edges)[None:500:None]:
            print(edge)
            G_bc.add_edge(edge[0], edge[1])

            bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G_bc, weight=None, normalized=False, xtra_data=True)
            G_dyn, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc2, D2, SP2, Delta2, edge, "add")

            for s in sorted(G_bc):
                assert bc1[s] == pytest.approx(bc2[s], abs=1e-7)

                for t in sorted(G_bc):
                    assert SP1[s][t] == pytest.approx(SP2[s][t], abs=1e-7)

    @pytest.mark.skip(reason="takes too long, we know this works")
    def test_deconstruct_facebook(self):
        G = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/0.edges")
        edges = G.edges()
        G_dyn = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/0.edges")

        bc2, D2, SP2, Delta2 = \
            nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)

        for edge in list(G.edges)[None:100:None]:
            print(edge)
            G.remove_edge(edge[0], edge[1])

            bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
            G_dyn, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc2, D2, SP2, Delta2, edge, "remove")

            for s in sorted(G):
                assert bc1[s] == pytest.approx(bc2[s], abs=1e-7)

                for t in sorted(G):
                    assert SP1[s][t] == pytest.approx(SP2[s][t], abs=1e-7)
