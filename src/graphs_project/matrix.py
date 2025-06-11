from graph import Graph


class MatrixGraph(Graph):
    def __init__(self, directed=False):
        super().__init__(directed)
        self.vertices = []
        self.matrix = []

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            return
        self.vertices.append(vertex)
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * len(self.vertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        idx1 = self.vertices.index(v1)
        idx2 = self.vertices.index(v2)
        self.matrix[idx1][idx2] = weight
        if not self.directed:
            self.matrix[idx2][idx1] = weight

    def remove_vertex(self, vertex):
        if vertex not in self.vertices:
            return
        idx = self.vertices.index(vertex)
        self.vertices.pop(idx)
        self.matrix.pop(idx)
        for row in self.matrix:
            row.pop(idx)

    def remove_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            idx1 = self.vertices.index(v1)
            idx2 = self.vertices.index(v2)
            self.matrix[idx1][idx2] = 0
            if not self.directed:
                self.matrix[idx2][idx1] = 0
