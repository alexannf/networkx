import pytest
import networkx as nx
import networkx.algorithms.thesis_Alex.utils.graphs as g
from networkx.algorithms.thesis_Alex.thesis_algo_old import dynamic_group_betweenness
from networkx.algorithms.thesis_Alex.setup import get_groups


class TestThesisGroupBetweenness:

    def test_edge_addition_existing_nodes(self):
        G = g.complete_square()
        G_dyn = g.incomplete_square()
        groups = ['1', '2']

        GBC_in, bc_in, PB_in, D_in, sigma_in, Delta_in = nx.group_betweenness_centrality(
            G_dyn, groups, normalized=False, endpoints=True, xtra_data=True)

        GBC_new, G_new, bc_new, PB_new, D_new, sigma_new, Delta_new = \
            dynamic_group_betweenness(
                G_dyn, groups, bc_in, D_in, sigma_in, Delta_in, ('3', '4'), "add", normalized=False, endpoints=True)

        GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(
            G, groups, normalized=False, endpoints=True, xtra_data=True)

        assert pytest.approx(GBC_new, abs=1e-7) == GBC

        for s in sorted(G_new):

            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(sigma_new[s][t], abs=1e-7) == sigma[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_edge_removal_existing_nodes(self):
        G = g.incomplete_square()
        G_dyn = g.complete_square()
        groups = ['1', '2']

        GBC_in, bc_in, PB_in, D_in, sigma_in, Delta_in = nx.group_betweenness_centrality(
            G_dyn, groups, normalized=False, endpoints=True, xtra_data=True)

        GBC_new, G_new, bc_new, PB_new, D_new, sigma_new, Delta_new = \
            dynamic_group_betweenness(
                G_dyn, groups, bc_in, D_in, sigma_in, Delta_in, ('3', '4'), "remove", normalized=False, endpoints=True)

        GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(
            G, groups, normalized=False, endpoints=True, xtra_data=True)

        assert pytest.approx(GBC_new, abs=1e-7) == GBC

        for s in sorted(G_new):
            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(sigma_new[s][t], abs=1e-7) == sigma[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_edge_addition_trondheim_graph(self):
        G = g.trondheim_graph()
        G.add_edge('5', 'F')
        G_dyn = g.trondheim_graph()
        G_dyn.add_edge('5', 'F')
        G_dyn.remove_edge('5', 'F')
        groups = [['D', '12'], ['D', 'L'], ['L', '2']]

        GBC_in, bc_in, PB_in, D_in, sigma_in, Delta_in = nx.group_betweenness_centrality(
            G_dyn, groups, normalized=False, endpoints=True, xtra_data=True)

        GBC_new, G_new, bc_new, PB_new, D_new, sigma_new, Delta_new = \
            dynamic_group_betweenness(
                G_dyn, groups, bc_in, D_in, sigma_in, Delta_in, ('5', 'F'), "add", normalized=False, endpoints=True)

        GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(
            G, groups, normalized=False, endpoints=True, xtra_data=True)

        for group_dyn, group in zip(GBC_new, GBC):
            assert pytest.approx(group_dyn, abs=1e-7) == group

        for s in sorted(G_new):
            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(sigma_new[s][t], abs=1e-7) == sigma[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_edge_deletion_trondheim_graph(self):
        G = g.trondheim_graph()
        G.remove_edge('1', '2')
        G_dyn = g.trondheim_graph()
        groups = [['D', '12'], ['D', 'L'], ['L', '2']]

        GBC_in, bc_in, PB_in, D_in, sigma_in, Delta_in = nx.group_betweenness_centrality(
            G_dyn, groups, normalized=False, endpoints=True, xtra_data=True)

        GBC_new, G_new, bc_new, PB_new, D_new, sigma_new, Delta_new = \
            dynamic_group_betweenness(
                G_dyn, groups, bc_in, D_in, sigma_in, Delta_in, ('1', '2'), "remove", normalized=False, endpoints=True)

        GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(
            G, groups, normalized=False, endpoints=True, xtra_data=True)

        for group_dyn, group in zip(GBC_new, GBC):
            assert pytest.approx(group_dyn, abs=1e-7) == group

        for s in sorted(G_new):
            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(sigma_new[s][t], abs=1e-7) == sigma[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_edge_reconnection_disconnected_graph_trondheim(self):
        G = g.trondheim_graph()
        G_dyn = g.trondheim_graph()
        groups = [['D', '12'], ['D', 'L'], ['L', '2']]

        GBC, bc, PB, D, sigma, Delta = nx.group_betweenness_centrality(
            G, groups, normalized=False, endpoints=True, xtra_data=True)

        GBC_in, bc_in, PB_in, D_in, sigma_in, Delta_in = nx.group_betweenness_centrality(
            G_dyn, groups, normalized=False, endpoints=True, xtra_data=True)

        GBC_new, G_new, bc_new, PB_new, D_new, sigma_new, Delta_new = \
            dynamic_group_betweenness(
                G_dyn, groups, bc_in, D_in, sigma_in, Delta_in, ('B', 'D'), "remove", normalized=False, endpoints=True)

        GBC_new, G_new, bc_new, PB_new, D_new, sigma_new, Delta_new = \
            dynamic_group_betweenness(
                G_new, groups, bc_new, D_new, sigma_new, Delta_new, ('B', 'D'), "add", normalized=False, endpoints=True)

        for group_dyn, group in zip(GBC_new, GBC):
            assert pytest.approx(group_dyn, abs=1e-7) == group

        for s in sorted(G_new):

            for t in sorted(G):
                assert pytest.approx(D_new[s][t], abs=1e-7) == D[s][t]
                assert pytest.approx(sigma_new[s][t], abs=1e-7) == sigma[s][t]
                assert pytest.approx(Delta_new[s][t], abs=1e-7) == Delta[s][t]

    def test_construct_facebook_0(self):
        G = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/0.edges")
        edges = list(G.edges)[None:1500:None]
        edge_stream = list(map(lambda x: "{} {}".format(x[0], x[1]), edges))
        G_dyn = nx.parse_edgelist(edge_stream)
        G_bc = nx.parse_edgelist(edge_stream)
        groups = get_groups(G_bc, 5, 5)

        GBC2, bc2, PB2, D2, sigma2, Delta2 = nx.group_betweenness_centrality(
            G_dyn, groups, normalized=False, endpoints=True, xtra_data=True)

        for edge in list(G.edges)[1500:1515:None]:
            G_bc.add_edge(edge[0], edge[1])

            GBC1, bc1, PB1, D1, sigma1, Delta1 = nx.group_betweenness_centrality(
                G_bc, groups, normalized=False, endpoints=True, xtra_data=True)

            GBC2, G_dyn, bc2, PB2, D2, sigma2, Delta2 = \
                dynamic_group_betweenness(
                    G_dyn, groups, bc2, D2, sigma2, Delta2, edge, "add", normalized=False,
                    endpoints=True)

            for group_dyn, group in zip(GBC2, GBC1):
                assert pytest.approx(group_dyn, abs=1e-7) == group

            for s in sorted(G_bc):
                for t in sorted(G_bc):
                    if t not in D1[s]:
                        D1[s][t], Delta1[s][t] = float("inf"), 0
                    if t not in D2[s]:
                        D2[s][t], Delta2[s][t] = float("inf"), 0
                    assert pytest.approx(D2[s][t], abs=1e-7) == D1[s][t]
                    assert pytest.approx(sigma2[s][t], abs=1e-7) == sigma1[s][t]
                    assert pytest.approx(Delta2[s][t], abs=1e-7) == Delta1[s][t]

    def test_deconstruct_facebook(self):
        G = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/0.edges")
        G_dyn = nx.read_edgelist("C:/Users/alex/networkX/Datasets/facebook/0.edges")
        groups = get_groups(G, 3, 3)

        GBC2, bc2, PB2, D2, sigma2, Delta2 = nx.group_betweenness_centrality(
            G_dyn, groups, normalized=False, endpoints=True, xtra_data=True)

        for edge in list(G.edges)[None:5:None]:
            G.remove_edge(edge[0], edge[1])

            GBC1, bc1, PB1, D1, sigma1, Delta1 = nx.group_betweenness_centrality(
                G, groups, normalized=False, endpoints=True, xtra_data=True)

            GBC2, G_dyn, bc2, PB2, D2, sigma2, Delta2 = \
                dynamic_group_betweenness(
                    G_dyn, groups, bc2, D2, sigma2, Delta2, edge, "remove", normalized=False,
                    endpoints=True)

            for group_dyn, group in zip(GBC2, GBC1):
                assert pytest.approx(group_dyn, abs=1e-7) == group

            for s in sorted(G):
                for t in sorted(G):
                    if t not in D1[s]:
                        D1[s][t], Delta1[s][t] = float("inf"), 0
                    if t not in D2[s] or t not in Delta2[s]:
                        D2[s][t], Delta2[s][t] = float("inf"), 0
                    assert pytest.approx(D2[s][t], abs=1e-7) == D1[s][t]
                    assert pytest.approx(sigma2[s][t], abs=1e-7) == sigma1[s][t]
                    assert pytest.approx(Delta2[s][t], abs=1e-7) == Delta1[s][t]
