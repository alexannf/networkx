import pytest
import networkx as nx
import networkx.algorithms.thesis_Alex.utils.graphs as g
from networkx.algorithms.thesis_Alex.thesis_algo import dynamic_group_betweenness


class TestThesisGroupBetweenness:

    def test_edge_addition_existing_nodes(self):
        G = g.complete_square()
        G_dyn = g.incomplete_square()
        groups = ['1', '2']

        GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(
            G, groups, normalized=False, endpoints=True, xtra_data=True)

        GBC_in, bc_in, PB_in, D_in, sigma_in, Delta_in = nx.group_betweenness_centrality(
            G_dyn, groups, normalized=False, endpoints=True, xtra_data=True)

        GBC_new, G_new, bc_new, PB_new, D_new, sigma_new, Delta_new = \
            dynamic_group_betweenness(
                G_dyn, groups, bc_in, D_in, sigma_in, Delta_in, ('3', '4'), "add", normalized=False, endpoints=True)



        # assert pytest.approx(GBC_new, abs=1e-7) == GBC

        for s in sorted(G_new):
            assert pytest.approx(bc_new[s], abs=1e-7) == bc[s]

            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(sigma_new[s][t], abs=1e-7) ==sigma[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_edge_removal_existing_nodes(self):
        G = g.incomplete_square()
        G_dyn = g.complete_square()

        bc, D, SP, Delta = nx.betweenness_centrality(G, endpoints=True, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('3', '4'), "remove", endpoints=True)

        for s in sorted(G):
            assert pytest.approx(bc_new[s], abs=1e-7) == bc[s]

            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(SP_new[s][t], abs=1e-7) == SP[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_edge_addition_trondheim_graph(self):
        G = g.trondheim_graph()
        G.add_edge('5', 'F')
        G_dyn = g.trondheim_graph()
        G_dyn.add_edge('5', 'F')
        G_dyn.remove_edge('5', 'F')

        bc, D, SP, Delta = nx.betweenness_centrality(G, endpoints=True, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('5', 'F'), "add", endpoints=True)

        for s in sorted(G):
            assert pytest.approx(bc_new[s], abs=1e-7) == bc[s]

            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(SP_new[s][t], abs=1e-7) == SP[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_edge_deletion_trondheim_graph(self):
        G = g.trondheim_graph()
        G.remove_edge('1', '2')
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, endpoints=True, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('1', '2'), "remove", endpoints=True)

        for s in sorted(G):
            assert pytest.approx(bc_new[s], abs=1e-7) == bc[s]

            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(SP_new[s][t], abs=1e-7) == SP[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_edge_reconnection_disconnected_graph_line(self):
        G = g.line_length_5()
        G_dyn = g.line_length_5()

        bc, D, SP, Delta = nx.betweenness_centrality(G, endpoints=True, normalized=False, xtra_data=True)
        G_rem, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc, D, SP, Delta, ('3', '4'), "remove")
        G_dyn, bc3, D3, SP3, Delta3 = nx.algorithm_1(G_rem, bc2, D2, SP2, Delta2, ('3', '4'), "add")

        for s in sorted(G):
            assert pytest.approx(bc3[s], abs=1e-7) == bc[s]

            for t in sorted(G):
                assert pytest.approx(SP3[s][t], abs=1e-7) == SP[s][t]

    def test_edge_reconnection_disconnected_graph_trondheim(self):
        G = g.trondheim_graph()
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, endpoints=True, normalized=False, xtra_data=True)
        G_rem, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc, D, SP, Delta, ('B', 'D'), "remove")
        G_dyn, bc3, D3, SP3, Delta3 = nx.algorithm_1(G_rem, bc2, D2, SP2, Delta2, ('B', 'D'), "add")

        for s in sorted(G):
            assert pytest.approx(bc3[s], abs=1e-7) == bc[s]

            for t in sorted(G):
                assert pytest.approx(SP3[s][t], abs=1e-7) == SP[s][t]

    def test_construct_facebook_0(self):
        G = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/0.edges")
        edges = list(G.edges)[None:1500:None]
        edge_stream = list(map(lambda x: "{} {}".format(x[0], x[1]), edges))
        G_dyn = nx.parse_edgelist(edge_stream)
        G_bc = nx.parse_edgelist(edge_stream)

        bc2, D2, SP2, Delta2 = \
            nx.betweenness_centrality(G_dyn, endpoints=True, normalized=False, xtra_data=True)

        for edge in list(G.edges)[1500:1530:None]:
            G_bc.add_edge(edge[0], edge[1])

            bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G_bc, endpoints=True, normalized=False, xtra_data=True)
            G_dyn, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc2, D2, SP2, Delta2, edge, "add")

            for s in sorted(G_bc):
                assert pytest.approx(bc2[s], abs=1e-7) == bc1[s]

                for t in sorted(G_bc):
                    assert pytest.approx(SP2[s][t], abs=1e-7) == SP1[s][t]

    def test_deconstruct_facebook(self):
        G = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/0.edges")
        G_dyn = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/0.edges")

        bc2, D2, SP2, Delta2 = \
            nx.betweenness_centrality(G, endpoints=True, normalized=False, xtra_data=True)

        for edge in list(G.edges)[None:10:None]:
            G.remove_edge(edge[0], edge[1])

            bc1, D1, SP1, Delta1 = nx.betweenness_centrality(G, endpoints=True, normalized=False, xtra_data=True)
            G_dyn, bc2, D2, SP2, Delta2 = nx.algorithm_1(G_dyn, bc2, D2, SP2, Delta2, edge, "remove")

            for s in sorted(G):
                assert pytest.approx(bc2[s], abs=1e-7) == bc1[s]

                for t in sorted(G):
                    assert pytest.approx(SP2[s][t], abs=1e-7) == SP1[s][t]

