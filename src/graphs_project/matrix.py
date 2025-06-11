from graphs_project.graph import Graph
from graphs_project.vertex import Vertex


class MatrixGraph(Graph):

    # 1. Representação de grafos utilizando Matriz de Adjacência (classe e atributos)
    def __init__(self, directed=False):
        super().__init__(directed)
        self.vertices: list[Vertex] = []
        self.vertices: list[Vertex] = []
        self.matrix = []

    # 2. Criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)
    # 2.1. Adicionando 1 vértice (método auxiliar)
    def add_vertex(self, vertex):
        if any(v.id == vertex.id for v in self.vertices):
            print(f"Vértice '{vertex.id}' já existe.")
            return

        self.vertices.append(vertex)

        for row in self.matrix:
            row.append(0)

        self.matrix.append([0] * len(self.vertices))

    # 2.2. Adicionando quantos vértices o usuário quiser
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

    # 3. Criação de aresta
    def add_edge(self):
        try:
            v1_id = input("ID do vértice de origem: ").strip()
            v2_id = input("ID do vértice de destino: ").strip()
            peso_input = input("Peso (pressione Enter para usar 1): ").strip()
            weight = float(peso_input) if peso_input else 1

            # Verifica se os vértices já existem
            ids = [v.id for v in self.vertices]

            if v1_id not in ids:
                self.add_vertex(Vertex(v1_id))
            if v2_id not in ids:
                self.add_vertex(Vertex(v2_id))

            idx1 = ids.index(v1_id)
            idx2 = ids.index(v2_id)

            self.matrix[idx1][idx2] = weight
            if not self.directed:
                self.matrix[idx2][idx1] = weight

            print(f"Aresta adicionada: {v1_id} -> {v2_id} (peso {weight})")

        except ValueError:
            print("Peso inválido. A aresta não foi criada.")

    # 4. Remoção de aresta
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            idx1 = self.vertices.index(vertex1)
            idx2 = self.vertices.index(vertex2)
            self.matrix[idx1][idx2] = 0
            if not self.directed:
                self.matrix[idx2][idx1] = 0

    # 5. Ponderação e rotulação de vértices

    # 6. Ponderação e rotulação de arestas

    # 7. Checagem de adjacência entre vértices

    # 8. Checagem de adjacência entre arestas

    # 9. Checagem de incidência entre aresta e vértice

    # 10. Checagem da existência de arestas

    # 11. Checagem da quantidade de vértices e arestas

    # 12. Checagem de grafo vazio e completo

    # 13. Métodos extras
    def display(self):
        print("Matriz de Adjacência:")
        print("   ", " ".join(v.id for v in self.vertices))
        for i, row in enumerate(self.matrix):
            print(self.vertices[i].id, row)
