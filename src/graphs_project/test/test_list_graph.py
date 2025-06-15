from graphs_project.list import ListGraph
import unittest

class TestListGraph(unittest.TestCase):
    def setUp(self):
        self.g = ListGraph(directed=False)

    def test_add_vertex(self):
        v = self.g.lib_add_vertex("X")
        print(f"Vertex adicionado: id={v.id}")
        self.assertEqual(v.id, "X")

    def test_add_duplicate_vertex(self):
        self.g.lib_add_vertex("X")
        with self.assertRaises(ValueError):
            self.g.lib_add_vertex("X")

    def test_add_vertices(self):
        v = self.g.lib_add_vertices(3)
        print(f"Vertices adicionados: {[vert.id for vert in v]}")
        self.assertEqual(len(v), 3)
        self.assertEqual(v[0].id, "V0")
        self.assertEqual(v[1].id, "V1")
        self.assertEqual(v[2].id, "V2")

    def test_add_vertices_invalid_count(self):
        with self.assertRaises(ValueError):
            self.g.lib_add_vertices(0)

    def test_add_edge_between_existing(self):
        self.g.lib_add_vertex("A")
        self.g.lib_add_vertex("B")
        e = self.g.lib_add_edge("A", "B", weight=2.0, label="A-B")
        print(f"Aresta adicionada: {e.sourceVertex.id} -> {e.targetVertex.id}, peso={e.weight}, rótulo={e.label}")
        self.assertEqual(e.sourceVertex.id, "A")
        self.assertEqual(e.targetVertex.id, "B")
        self.assertEqual(e.weight, 2.0)
        self.assertEqual(e.label, "A-B")

    def test_add_edge_creates_vertices(self):
        e = self.g.lib_add_edge("A", "B")
        print(f"Aresta criada com vértices implícitos: {e.sourceVertex.id} -> {e.targetVertex.id}")
        self.assertEqual(e.sourceVertex.id, "A")
        self.assertEqual(e.targetVertex.id, "B")

    def test_remove_edge_by_label(self):
        self.g.lib_add_edge("A", "B", label="x")
        r = self.g.lib_remove_edge(label="x")
        print(f"Aresta removida pelo rótulo: {r.label}")
        self.assertEqual(r.label, "x")

    def test_remove_edge_by_vertices(self):
        self.g.lib_add_edge("A", "B")
        r = self.g.lib_remove_edge("A", "B")
        print(f"Aresta removida por vértices: {r.sourceVertex.id} -> {r.targetVertex.id}")
        self.assertEqual(r.sourceVertex.id, "A")
        self.assertEqual(r.targetVertex.id, "B")

    def test_remove_edge_not_found(self):
        with self.assertRaises(ValueError):
            self.g.lib_remove_edge("X", "Y")

    def test_set_vertex_weight(self):
        self.g.lib_add_vertex("A")
        v = self.g.lib_set_vertex_weight("A", 10.5)
        print(f"Peso do vértice 'A' setado para: {v.weight}")
        self.assertEqual(v.weight, 10.5)

    def test_set_vertex_label(self):
        self.g.lib_add_vertex("A")
        v = self.g.lib_set_vertex_label("A", "rótulo")
        print(f"Rótulo do vértice 'A': {v.label}")
        self.assertEqual(v.label, "rótulo")

    def test_set_vertex_invalid(self):
        with self.assertRaises(ValueError):
            self.g.lib_set_vertex_weight("Z", 1)
        with self.assertRaises(ValueError):
            self.g.lib_set_vertex_label("Z", "algo")

    def test_set_edge_weight_by_label(self):
        self.g.lib_add_edge("A", "B", label="lab")
        e = self.g.lib_set_edge_weight(3.5, label="lab")
        print(f"Peso da aresta 'lab' setado para: {e.weight}")
        self.assertEqual(e.weight, 3.5)

    def test_set_edge_weight_by_vertices(self):
        self.g.lib_add_edge("A", "B")
        e = self.g.lib_set_edge_weight(4.0, source_id="A", target_id="B")
        print(f"Peso da aresta A-B setado para: {e.weight}")
        self.assertEqual(e.weight, 4.0)

    def test_set_edge_label_by_old_label(self):
        self.g.lib_add_edge("A", "B", label="old")
        e = self.g.lib_set_edge_label("new", old_label="old")
        print(f"Rótulo da aresta alterado de 'old' para '{e.label}'")
        self.assertEqual(e.label, "new")

    def test_set_edge_label_by_vertices(self):
        self.g.lib_add_edge("A", "B")
        e = self.g.lib_set_edge_label("nova", source_id="A", target_id="B")
        print(f"Rótulo da aresta A-B setado para: {e.label}")
        self.assertEqual(e.label, "nova")

    def test_set_edge_invalid(self):
        with self.assertRaises(ValueError):
            self.g.lib_set_edge_weight(1.1, source_id="X", target_id="Y")
        with self.assertRaises(ValueError):
            self.g.lib_set_edge_label("abc")

if __name__ == "__main__":
    unittest.main()
