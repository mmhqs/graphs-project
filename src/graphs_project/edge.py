class Edge:
    # Atributo da classe para contar as arestas
    _id_counter = 0

    # Atributos da aresta
    def __init__(self, source, target, weight=1, label=None):
        self.id = Edge._id_counter
        Edge._id_counter += 1  # incrementa para a próxima aresta
        self.sourceVertex = source
        self.targetVertex = target
        self.weight = weight
        self.label = label

    def __repr__(self):
        return f"Edge(id={self.id}, source={self.sourceVertex.id}, target={self.targetVertex.id}, weight={self.weight}, label={self.label})"
