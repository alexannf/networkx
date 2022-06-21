import pytest
import networkx as nx
import networkx.algorithms.thesis_Alex.utils.graphs as g





class TestKourtellisBetweenness:


    def test_edge_addition_existing_nodes(self):
        G = g.complete_square()
        G_dyn = g.incomplete_square()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('3', '4'), "add")

        for n in sorted(G):
            assert bc[n] == pytest.approx(bc_new[n], abs=1e-7)
            assert D[n] == pytest.approx(D_new[n], abs=1e-7)
            assert SP[n] == pytest.approx(SP_new[n], abs=1e-7)
            assert Delta[n] == pytest.approx(Delta_new[n], abs=1e-7)

    def test_edge_removal_existing_nodes(self):
        G = g.incomplete_square()
        G_dyn = g.complete_square()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('3', '4'), "remove")

        for n in sorted(G):
            assert bc[n] == pytest.approx(bc_new[n], abs=1e-7)
            assert D[n] == pytest.approx(D_new[n], abs=1e-7)
            assert SP[n] == pytest.approx(SP_new[n], abs=1e-7)
            assert Delta[n] == pytest.approx(Delta_new[n], abs=1e-7)

    def test_edge_addition_trondheim_graph(self):
        G = g.trondheim_graph()
        G.add_edge('5', 'F')
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('5', 'F'), "add")

        for n in sorted(G):
            assert bc[n] == pytest.approx(bc_new[n], abs=1e-7)
            assert D[n] == pytest.approx(D_new[n], abs=1e-7)
            assert SP[n] == pytest.approx(SP_new[n], abs=1e-7)
            assert Delta[n] == pytest.approx(Delta_new[n], abs=1e-7)

    def test_edge_deletion_trondheim_graph(self):
        G = g.trondheim_graph()
        G.remove_edge('1', '2')
        G_dyn = g.trondheim_graph()

        bc, D, SP, Delta = nx.betweenness_centrality(G, weight=None, normalized=False, xtra_data=True)
        G_new, bc_new, D_new, SP_new, Delta_new = nx.kourtellis_dynamic_bc(G_dyn, ('1', '2'), "remove")

        for n in sorted(G):
            assert bc[n] == pytest.approx(bc_new[n], abs=1e-7)
            assert D[n] == pytest.approx(D_new[n], abs=1e-7)
            assert SP[n] == pytest.approx(SP_new[n], abs=1e-7)
            assert Delta[n] == pytest.approx(Delta_new[n], abs=1e-7)
