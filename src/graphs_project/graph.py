from abc import ABC, abstractmethod


class Graph(ABC):
    def __init__(self, directed=False):
        self.directed = directed

    @abstractmethod
    def add_vertex(self, vertex):
        pass

    @abstractmethod
    def add_edge(self, v1, v2, weight=1):
        pass

    @abstractmethod
    def remove_vertex(self, vertex):
        pass

    @abstractmethod
    def remove_edge(self, v1, v2):
        pass
