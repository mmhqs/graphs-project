class Edge:
    # Atributos da aresta
    def __init__(self, source, target, weight=1.0, label=None):
        self.sourceVertex = source
        self.targetVertex = target
        self.weight = weight
        self.label = label

    def __repr__(self):
        return (f"Edge({self.sourceVertex} -> {self.targetVertex}, weight={self.weight}, "
                f"label={self.label})")
