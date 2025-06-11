class Vertex:
    # Atributos do vértice
    def __init__(self, id, label=None, weight=1.0):
        self.id = id              # identificador único (ex: "A", "B", "V0")
        self.label = label if label else id
        self.weight = weight

    def __repr__(self):
        return f"Vertex(id={self.id}, label={self.label}, weight={self.weight})"
