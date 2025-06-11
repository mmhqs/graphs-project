from graph import Graph
from graphs_project.vertex import Vertex


class MatrixGraph(Graph):
    # Representação de grafos utilizando Matriz de Adjacência (classe e atributos)
    def __init__(self, directed=False):
        super().__init__(directed)
        self.vertices: list[Vertex] = []
        self.matrix = []

    # Criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)
    def add_vertices(self):
        try:
            count = int(input("Digite o número de vértices: "))
            if count <= 0:
                print("O número de vértices deve ser positivo.")
                return

            for i in range(count):
                vertex_id = f"V{i}"
                vertex = Vertex(id=vertex_id)  # cria um objeto Vertex
                self.add_vertex(vertex)

            print(
                f"Grafo criado com {count} vértices: {[v.id for v in self.vertices]}")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Criação de aresta
    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)
        idx1 = self.vertices.index(vertex1)
        idx2 = self.vertices.index(vertex2)
        self.matrix[idx1][idx2] = weight
        if not self.directed:
            self.matrix[idx2][idx1] = weight

    # Remoção de aresta
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            idx1 = self.vertices.index(vertex1)
            idx2 = self.vertices.index(vertex2)
            self.matrix[idx1][idx2] = 0
            if not self.directed:
                self.matrix[idx2][idx1] = 0

    # Ponderação e rotulação de vértices

    # Ponderação e rotulação de arestas

    # Checagem de adjacência entre vértices

    # Checagem de adjacência entre arestas

    # Checagem de incidência entre aresta e vértice

    # Checagem da existência de arestas

    # Checagem da quantidade de vértices e arestas

    # Checagem de grafo vazio e completo
