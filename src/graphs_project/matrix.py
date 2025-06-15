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
    def check_vertex_adjacency(self):
        vertex1_id = input("ID do primeiro vértice: ").strip()
        vertex2_id = input("ID do segundo vértice: ").strip()
        
        ids = [v.id for v in self.vertices]
        
        if vertex1_id not in ids or vertex2_id not in ids:
            print("Um ou ambos os vértices não existem no grafo.")
            return
        
        idx1 = ids.index(vertex1_id)
        idx2 = ids.index(vertex2_id)
        
        # Verifica adjacência na matriz
        adjacent = self.matrix[idx1][idx2] != 0
        
        if self.directed:
            print(f"'{vertex1_id}' {'é' if adjacent else 'não é'} adjacente a '{vertex2_id}'")
        else:
            # Para grafos não direcionados, a adjacência é mútua
            adjacent_mutual = adjacent or self.matrix[idx2][idx1] != 0
            print(f"'{vertex1_id}' e '{vertex2_id}' {'são' if adjacent_mutual else 'não são'} adjacentes")

    # 8. Checagem de adjacência entre arestas
    def check_edge_adjacency(self):
        print("Identifique a primeira aresta:")
        edge1 = self._select_edge()
        if not edge1:
            return
        
        print("\nIdentifique a segunda aresta:")
        edge2 = self._select_edge()
        if not edge2:
            return
        
        # Duas arestas são adjacentes se compartilham um vértice comum
        adjacent = (edge1.sourceVertex == edge2.sourceVertex or
                    edge1.sourceVertex == edge2.targetVertex or
                    edge1.targetVertex == edge2.sourceVertex or
                    edge1.targetVertex == edge2.targetVertex)
        
        print(f"As arestas {'são' if adjacent else 'não são'} adjacentes")

    # Método auxiliar para selecionar aresta
    def _select_edge(self):
        print("Escolha como identificar a aresta:")
        print("1 - Por label")
        print("2 - Por vértices de origem e destino")
        
        try:
            opcao = int(input("Digite sua opção (1 ou 2): ").strip())
        except ValueError:
            print("Opção inválida.")
            return None

        if opcao == 1:
            label = input("Label da aresta: ").strip()
            for edge in self.edges:
                if edge.label == label:
                    return edge
            print("Aresta não encontrada.")
            return None
            
        elif opcao == 2:
            vertex1_id = input("ID do vértice de origem: ").strip()
            vertex2_id = input("ID do vértice de destino: ").strip()
            for edge in self.edges:
                if (edge.sourceVertex.id == vertex1_id and 
                    edge.targetVertex.id == vertex2_id):
                    return edge
            print("Aresta não encontrada.")
            return None
            
        else:
            print("Opção inválida.")
            return None

    # 9. Checagem de incidência entre aresta e vértice
    def check_incidence(self):
        vertex_id = input("ID do vértice: ").strip()
        print("\nIdentifique a aresta:")
        edge = self._select_edge()
        if not edge:
            return
        
        # Verifica se o vértice é um dos extremos da aresta
        incident = (edge.sourceVertex.id == vertex_id or 
                   edge.targetVertex.id == vertex_id)
        
        print(f"A aresta {'incide' if incident else 'não incide'} no vértice {vertex_id}")

    # 10. Checagem da existência de arestas
    def has_edges(self):
        if self.edges:
            print("O grafo possui arestas.")
        else:
            print("O grafo não possui arestas.")

    # 11. Checagem da quantidade de vértices e arestas
    def get_graph_size(self):
        num_vertices = len(self.vertices)
        num_edges = len(self.edges)
        print(f"O grafo possui {num_vertices} vértices e {num_edges} arestas.")

    # 12. Checagem de grafo vazio e completo
    def check_graph_type(self):
        # Grafo vazio
        if not self.edges:
            print("O grafo é vazio (não possui arestas).")
            return
        
        # Verifica se é completo
        num_vertices = len(self.vertices)
        max_edges = num_vertices * (num_vertices - 1)
        if not self.directed:
            max_edges = max_edges // 2
        
        if len(self.edges) == max_edges:
            print("O grafo é completo.")
        else:
            print("O grafo não é completo.")
    # 13. Métodos extras

    def display(self):
        print("\nMatriz de Adjacência:")
        print("   ", " ".join(v.id for v in self.vertices))
        for i, row in enumerate(self.matrix):
            print(self.vertices[i].id, row)

    # Versão lib das funções principais
    def lib_add_vertex(self, vertex_id: str) -> None:
        """
        Adiciona um vértice ao grafo usando o ID fornecido.
        
        Args:
            vertex_id (str): ID do vértice a ser adicionado
        """
        vertex = Vertex(id=vertex_id)
        if any(v.id == vertex.id for v in self.vertices):
            raise ValueError(f"Vértice '{vertex.id}' já existe.")

        self.vertices.append(vertex)
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * len(self.vertices))
        return vertex

    def lib_add_vertices(self, count: int) -> list[Vertex]:
        """
        Adiciona múltiplos vértices ao grafo.
        
        Args:
            count (int): Número de vértices a serem adicionados
            
        Returns:
            list[Vertex]: Lista dos vértices adicionados
        """
        if count <= 0:
            raise ValueError("O número de vértices deve ser positivo.")

        added_vertices = []
        for i in range(count):
            vertex_id = f"V{i}"
            vertex = self.lib_add_vertex(vertex_id)
            added_vertices.append(vertex)

        return added_vertices

    def lib_add_edge(self, source_id: str, target_id: str, weight: float = 1, label: str = None) -> Edge:
        """
        Adiciona uma aresta ao grafo.
        
        Args:
            source_id (str): ID do vértice de origem
            target_id (str): ID do vértice de destino
            weight (float, optional): Peso da aresta. Defaults to 1.
            label (str, optional): Rótulo da aresta. Defaults to None.
            
        Returns:
            Edge: A aresta criada
        """
        # Verifica se os vértices existem, senão cria
        if not any(v.id == source_id for v in self.vertices):
            self.lib_add_vertex(source_id)
        if not any(v.id == target_id for v in self.vertices):
            self.lib_add_vertex(target_id)

        ids = [v.id for v in self.vertices]
        idx1 = ids.index(source_id)
        idx2 = ids.index(target_id)

        self.matrix[idx1][idx2] = weight
        if not self.directed:
            self.matrix[idx2][idx1] = weight

        source_vertex = self.vertices[idx1]
        target_vertex = self.vertices[idx2]

        new_edge = Edge(source_vertex, target_vertex, weight, label)
        self.edges.append(new_edge)
        
        return new_edge

    def lib_remove_edge(self, source_id: str = None, target_id: str = None, label: str = None) -> Edge:
        """
        Remove uma aresta do grafo.
        
        Args:
            source_id (str, optional): ID do vértice de origem
            target_id (str, optional): ID do vértice de destino
            label (str, optional): Rótulo da aresta
            
        Returns:
            Edge: A aresta removida
        
        Raises:
            ValueError: Se a aresta não for encontrada
        """
        edge_to_remove = None

        if label is not None:
            for edge in self.edges:
                if edge.label == label:
                    edge_to_remove = edge
                    break
        elif source_id is not None and target_id is not None:
            for edge in self.edges:
                if (edge.sourceVertex.id == source_id and 
                    edge.targetVertex.id == target_id):
                    edge_to_remove = edge
                    break

        if not edge_to_remove:
            raise ValueError("Aresta não encontrada.")

        source_id = edge_to_remove.sourceVertex.id
        target_id = edge_to_remove.targetVertex.id

        ids = [v.id for v in self.vertices]
        idx1 = ids.index(source_id)
        idx2 = ids.index(target_id)

        self.matrix[idx1][idx2] = 0
        if not self.directed:
            self.matrix[idx2][idx1] = 0

        self.edges.remove(edge_to_remove)
        return edge_to_remove

    def lib_set_vertex_weight(self, vertex_id: str, weight: float) -> Vertex:
        """
        Define o peso de um vértice.
        
        Args:
            vertex_id (str): ID do vértice
            weight (float): Novo peso
            
        Returns:
            Vertex: O vértice atualizado
            
        Raises:
            ValueError: Se o vértice não for encontrado
        """
        for vertex in self.vertices:
            if vertex.id == vertex_id:
                vertex.weight = weight
                return vertex
        raise ValueError(f"Vértice '{vertex_id}' não encontrado.")

    def lib_set_vertex_label(self, vertex_id: str, label: str) -> Vertex:
        """
        Define o rótulo de um vértice.
        
        Args:
            vertex_id (str): ID do vértice
            label (str): Novo rótulo
            
        Returns:
            Vertex: O vértice atualizado
            
        Raises:
            ValueError: Se o vértice não for encontrado
        """
        for vertex in self.vertices:
            if vertex.id == vertex_id:
                vertex.label = label
                return vertex
        raise ValueError(f"Vértice '{vertex_id}' não encontrado.")

    def lib_set_edge_weight(self, weight: float, source_id: str = None, target_id: str = None, label: str = None) -> Edge:
        """
        Define o peso de uma aresta.
        
        Args:
            weight (float): Novo peso
            source_id (str, optional): ID do vértice de origem
            target_id (str, optional): ID do vértice de destino
            label (str, optional): Rótulo da aresta
            
        Returns:
            Edge: A aresta atualizada
            
        Raises:
            ValueError: Se a aresta não for encontrada
        """
        edge_to_update = None

        if label is not None:
            for edge in self.edges:
                if edge.label == label:
                    edge_to_update = edge
                    break
        elif source_id is not None and target_id is not None:
            for edge in self.edges:
                if (edge.sourceVertex.id == source_id and 
                    edge.targetVertex.id == target_id):
                    edge_to_update = edge
                    break

        if not edge_to_update:
            raise ValueError("Aresta não encontrada.")

        source_id = edge_to_update.sourceVertex.id
        target_id = edge_to_update.targetVertex.id

        ids = [v.id for v in self.vertices]
        idx1 = ids.index(source_id)
        idx2 = ids.index(target_id)

        self.matrix[idx1][idx2] = weight
        if not self.directed:
            self.matrix[idx2][idx1] = weight

        edge_to_update.weight = weight
        return edge_to_update

    def lib_set_edge_label(self, new_label: str, source_id: str = None, target_id: str = None, old_label: str = None) -> Edge:
        """
        Define o rótulo de uma aresta.
        
        Args:
            new_label (str): Novo rótulo
            source_id (str, optional): ID do vértice de origem
            target_id (str, optional): ID do vértice de destino
            old_label (str, optional): Rótulo atual da aresta
            
        Returns:
            Edge: A aresta atualizada
            
        Raises:
            ValueError: Se a aresta não for encontrada
        """
        edge_to_update = None

        if old_label is not None:
            for edge in self.edges:
                if edge.label == old_label:
                    edge_to_update = edge
                    break
        elif source_id is not None and target_id is not None:
            for edge in self.edges:
                if (edge.sourceVertex.id == source_id and 
                    edge.targetVertex.id == target_id):
                    edge_to_update = edge
                    break

        if not edge_to_update:
            raise ValueError("Aresta não encontrada.")

        edge_to_update.label = new_label
        return edge_to_update
