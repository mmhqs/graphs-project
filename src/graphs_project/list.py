from graphs_project.edge import Edge
from graphs_project.graph import Graph
from graphs_project.vertex import Vertex


class ListGraph(Graph):
    # 1. Representação de grafos utilizando Lista de Adjacência (classe e atributos)
    def __init__(self, directed=False):
        super().__init__(directed)
        self.vertices: list[Vertex] = []
        self.edges: list[Edge] = []
        self.adjacency_list = {}

    # 2. Criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)
   # 2.1. Adicionando 1 vértice (método auxiliar)
    def add_vertex(self, vertex):
        if any(v.id == vertex.id for v in self.vertices):
            print(f"Vértice '{vertex.id}' já existe.")
            return

        self.vertices.append(vertex)
        self.adjacency_list[vertex.id] = []  # Inicializa lista vazia de vizinhos

    # 2.2. Adicionando quantos vértices o usuário quiser
    def add_vertices(self):
        try:
            count = int(input("Digite o número de vértices: "))
            if count <= 0:
                print("O número de vértices deve ser positivo.")
                return

            for i in range(count):
                vertex_id = f"V{i}"
                vertex = Vertex(id=vertex_id)
                self.add_vertex(vertex)

            print(f"Grafo criado com {count} vértices: {[v.id for v in self.vertices]}")

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

            # Verifica se os vértices existem, senão cria
            if vertex1_id not in self.adjacency_list:
                self.add_vertex(Vertex(vertex1_id))
            if vertex2_id not in self.adjacency_list:
                self.add_vertex(Vertex(vertex2_id))

            # Adiciona à lista de adjacência
            neighbor_info = {'vertex_id': vertex2_id, 'weight': weight}
            self.adjacency_list[vertex1_id].append(neighbor_info)
            
            if not self.directed:
                neighbor_info_reverse = {'vertex_id': vertex1_id, 'weight': weight}
                self.adjacency_list[vertex2_id].append(neighbor_info_reverse)

            # Cria o objeto Edge
            source_vertex = next(v for v in self.vertices if v.id == vertex1_id)
            target_vertex = next(v for v in self.vertices if v.id == vertex2_id)
            new_edge = Edge(source_vertex, target_vertex, weight, label if label else None)
            print("new_edge")
            print(new_edge)
            self.edges.append(new_edge)

            print(f"Aresta adicionada: {vertex1_id} -> {vertex2_id} (peso {weight}, label: '{label if label else 'sem rótulo'}')")

        except ValueError:
            print("Peso inválido. A aresta não foi criada.")

    # 4. Remoção de aresta
    def remove_edge_aux(self, edge_to_remove, opcao):
        source_id = edge_to_remove.sourceVertex.id
        target_id = edge_to_remove.targetVertex.id

        # Remove da lista de adjacência
        self.adjacency_list[source_id] = [
            neighbor for neighbor in self.adjacency_list[source_id] 
            if neighbor['vertex_id'] != target_id
        ]
        
        if not self.directed:
            self.adjacency_list[target_id] = [
                neighbor for neighbor in self.adjacency_list[target_id] 
                if neighbor['vertex_id'] != source_id
            ]

        self.edges.remove(edge_to_remove)
        
        if opcao == 1:
            print(f"Aresta com label '{edge_to_remove.label if edge_to_remove.label else 'sem rótulo'}' removida com sucesso.")
        else:
            print(f"Aresta entre '{source_id}' e '{target_id}' removida com sucesso.")

    def remove_edge(self):
        print("Escolha o método de remoção:")
        print("1 - Remover por label")
        print("2 - Remover por vértices de origem e destino")
        
        try:
            opcao = int(input("Digite sua opção (1 ou 2): ").strip())
        except ValueError:
            print("Opção inválida. Operação cancelada.")
            return

        edge_to_remove = None

        if opcao == 1:
            label = input("Label da aresta a ser removida: ").strip()
            
            for edge in self.edges:
                if edge.label == label:
                    edge_to_remove = edge
                    break
            
            if not edge_to_remove:
                print(f"Aresta com label '{label}' não encontrada.")
                return

        elif opcao == 2:
            vertex1_id = input("ID do vértice de origem: ").strip()
            vertex2_id = input("ID do vértice de destino: ").strip()
            
            for edge in self.edges:
                if (edge.sourceVertex.id == vertex1_id and 
                    edge.targetVertex.id == vertex2_id):
                    edge_to_remove = edge
                    break
            
            if not edge_to_remove:
                print(f"Aresta entre '{vertex1_id}' e '{vertex2_id}' não encontrada.")
                return

        else:
            print("Opção inválida. Operação cancelada.")
            return
        
        self.remove_edge_aux(edge_to_remove, opcao)

        
    # 5. Ponderação e rotulação de vértices
    def set_vertex_weight(self):
        return;
    
    def set_vertex_label(self):
        return;

    # 6. Ponderação e rotulação de arestas
    def set_edge_weight(self):
        return;

    def set_edge_label(self):
        return;

    # 7. Checagem de adjacência entre vértices
    # 8. Checagem de adjacência entre arestas

    # 9. Checagem de incidência entre aresta e vértice

    # 10. Checagem da existência de arestas

    # 11. Checagem da quantidade de vértices e arestas

    # 12. Checagem de grafo vazio e completo

    # 13. Métodos extras

    def display(self):
        print("\nLista de Adjacência:")
        for vertex_id, neighbors in self.adjacency_list.items():
            if neighbors:
                neighbors_str = ", ".join([f"{n['vertex_id']}(peso:{n['weight']})" for n in neighbors])
                print(f"{vertex_id}: [{neighbors_str}]")
            else:
                print(f"{vertex_id}: []")