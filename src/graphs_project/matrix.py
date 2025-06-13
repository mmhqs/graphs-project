from graphs_project.edge import Edge
from graphs_project.graph import Graph
from graphs_project.vertex import Vertex


class MatrixGraph(Graph):

    # 1. Representação de grafos utilizando Matriz de Adjacência (classe e atributos)
    def __init__(self, directed=False):
        super().__init__(directed)
        self.vertices: list[Vertex] = []
        self.edges: list[Edge] = []
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
            vertex1_id = input("ID do vértice de origem: ").strip()
            vertex2_id = input("ID do vértice de destino: ").strip()
            peso_input = input("Peso (pressione Enter para usar 1): ").strip()
            label = input("Label da aresta (opcional): ").strip()
            weight = float(peso_input) if peso_input else 1

            ids = [v.id for v in self.vertices]

            if vertex1_id not in ids:
                self.add_vertex(Vertex(vertex1_id))
                ids = [v.id for v in self.vertices]  # atualiza após inserção
            if vertex2_id not in ids:
                self.add_vertex(Vertex(vertex2_id))
                ids = [v.id for v in self.vertices]

            idx1 = ids.index(vertex1_id)
            idx2 = ids.index(vertex2_id)

            self.matrix[idx1][idx2] = weight
            if not self.directed:
                self.matrix[idx2][idx1] = weight

            source_vertex = self.vertices[idx1]
            target_vertex = self.vertices[idx2]

            new_edge = Edge(source_vertex, target_vertex,
                            weight, label if label else None)
            
            self.edges.append(new_edge)

            print(
                f"Aresta adicionada: {vertex1_id} -> {vertex2_id} "
                f"(peso {weight}, label: '{label if label else 'sem rótulo'}')"
            )
            print("Arestas restantes no grafo:")
            if not self.edges:
                print("Nenhuma aresta.")
            else:
                for edge in self.edges:
                    print(
                        f"Label: {edge.label if edge.label else 'sem rótulo'} | "
                        f"{edge.sourceVertex.id} -> {edge.targetVertex.id} | "
                        f"Peso: {edge.weight}"
                    )

        except ValueError:
            print("Peso inválido. A aresta não foi criada.")

    # 4. Remoção de aresta
    def remove_edge(self):
        label = input("Label da aresta a ser removida: ").strip()

        edge_to_remove = None
        for edge in self.edges:
            if edge.label == label:
                edge_to_remove = edge
                break

        if not edge_to_remove:
            print(f"Aresta com label '{label}' não encontrada.")
            return

        source_id = edge_to_remove.sourceVertex.id
        target_id = edge_to_remove.targetVertex.id

        ids = [v.id for v in self.vertices]
        idx1 = ids.index(source_id)
        idx2 = ids.index(target_id)

        self.matrix[idx1][idx2] = 0
        if not self.directed:
            self.matrix[idx2][idx1] = 0

        self.edges.remove(edge_to_remove)
        print(f"Aresta com label '{label}' removida com sucesso.\n")

        print("Arestas restantes no grafo:")
        if not self.edges:
            print("Nenhuma aresta.")
        else:
            for edge in self.edges:
                print(
                    f"Label: {edge.label if edge.label else 'sem rótulo'} | "
                    f"{edge.sourceVertex.id} -> {edge.targetVertex.id} | "
                    f"Peso: {edge.weight}"
                )

    # 5. Ponderação e rotulação de vértices
    # 5.1. Ponderação
    def set_vertex_weight(self):
        vertex_id = input("ID do vértice: ").strip()
        peso_input = input("Peso a atribuir: ").strip()
        try:
            weight = int(peso_input)
        except ValueError:
            print("Peso inválido.")
            return

        for vertex in self.vertices:
            if vertex.id == vertex_id:
                vertex.weight = weight
                print(f"Peso {weight} atribuído ao vértice '{vertex_id}'.")

                print("Lista de vértices com seus pesos:")
                for v in self.vertices:
                    print(f"Vértice {v.id}: peso = {v.weight}")
                return
        print(f"Vértice '{vertex_id}' não encontrado.")

    # 5.2. Rotulação
    def set_vertex_label(self):
        vertex_id = input("ID do vértice: ").strip()
        label_input = input("Rótulo a atribuir: ").strip()

        for vertex in self.vertices:
            if vertex.id == vertex_id:
                vertex.label = label_input
                print(
                    f"\nRótulo {label_input} atribuído ao vértice '{vertex_id}'.")

                print("Lista de vértices com seus rótulos:")
                for v in self.vertices:
                    print(f"Vértice {v.id}: rótulo = {v.label}")
                return
        print(f"Vértice '{vertex_id}' não encontrado.")

    # 6. Ponderação e rotulação de arestas
    # 6.1 Ponderação
    def set_edge_weight(self):
        label = input("Label da aresta a ser atualizada: ").strip()
        weight_input = input("Novo peso da aresta: ").strip()

        try:
            weight = float(weight_input)
        except ValueError:
            print("Peso inválido. Operação cancelada.")
            return

        for edge in self.edges:
            if edge.label == label:
                source_id = edge.sourceVertex.id
                target_id = edge.targetVertex.id

                ids = [v.id for v in self.vertices]
                idx1 = ids.index(source_id)
                idx2 = ids.index(target_id)

                self.matrix[idx1][idx2] = weight
                if not self.directed:
                    self.matrix[idx2][idx1] = weight

                edge.weight = weight

                print(
                    f"\nPeso da aresta '{label}' atualizado para {weight}.\n")
                break
        else:
            print(f"Aresta com label '{label}' não encontrada.")
            return

        print("Lista atualizada de arestas com seus pesos:")
        for e in self.edges:
            print(
                f"Label: {e.label if e.label else 'sem rótulo'} | "
                f"{e.sourceVertex.id} -> {e.targetVertex.id} | "
                f"Peso: {e.weight}"
            )

    # 6.2. Rotulação
    def set_edge_label(self):
        label_atual = input("\nLabel da aresta que deseja renomear: ").strip()
        novo_label = input("Novo label para a aresta: ").strip()

        for edge in self.edges:
            if edge.label == label_atual:
                edge.label = novo_label
                print(
                    f"\nLabel da aresta atualizada de '{label_atual}' para '{novo_label}'.\n")
                break
        else:
            print(f"Nenhuma aresta encontrada com o label '{label_atual}'.")
            return

        print("Lista atualizada de arestas com seus rótulos:")
        for e in self.edges:
            print(
                f"Aresta {e.id}: "
                f"{e.sourceVertex.id} -> {e.targetVertex.id} | "
                f"Peso: {e.weight} | Rótulo: {e.label if e.label else 'sem rótulo'}"
            )

    # 7. Checagem de adjacência entre vértices

    # 8. Checagem de adjacência entre arestas

    # 9. Checagem de incidência entre aresta e vértice

    # 10. Checagem da existência de arestas

    # 11. Checagem da quantidade de vértices e arestas

    # 12. Checagem de grafo vazio e completo

    # 13. Métodos extras

    def display(self):
        print("\nMatriz de Adjacência:")
        print("   ", " ".join(v.id for v in self.vertices))
        for i, row in enumerate(self.matrix):
            print(self.vertices[i].id, row)
