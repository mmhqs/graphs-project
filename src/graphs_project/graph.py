from abc import ABC, abstractmethod


class Graph(ABC):
    # Atributos do grafo
    def __init__(self, directed=False):
        self.directed = directed

    # Criação de aresta
    @abstractmethod
    def add_edge(self, vertex1, vertex2, weight=1):
        pass

    # Remoção de aresta
    @abstractmethod
    def remove_edge(self, vertex1, vertex2):
        pass
