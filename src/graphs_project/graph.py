from abc import ABC, abstractmethod
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

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


    def export_to_gexf(self, filename):
    
        if not filename.lower().endswith('.gexf'):
            filename += '.gexf'

        root = Element('gexf', xmlns="http://www.gexf.net/1.2draft", version="1.2")
        
        # Meta dados devem vir antes do graph
        meta = SubElement(root, 'meta', lastmodifieddate="2023-11-25")
        SubElement(meta, 'creator').text = "Graphs Project"
        SubElement(meta, 'description').text = "Grafo exportado com labels"

        graph = SubElement(root, 'graph', defaultedgetype="directed" if self.directed else "undirected")

        # Nós (vértices)
        nodes = SubElement(graph, 'nodes')
        for vertex in self.vertices:
            # Usa o label do vértice se existir, senão usa o ID
            label = getattr(vertex, 'label', None) or vertex.id
            node = SubElement(nodes, 'node', id=str(vertex.id), label=str(label))
            
            # Adiciona peso como atributo se existir
            if hasattr(vertex, 'weight') and vertex.weight is not None:
                attvalues = SubElement(node, 'attvalues')
                SubElement(attvalues, 'attvalue', {'for': 'weight', 'value': str(vertex.weight)})

        # Arestas
        edges = SubElement(graph, 'edges')
        for edge_id, edge in enumerate(self.edges):
            edge_attrs = {
                'id': str(edge_id),
                'source': str(edge.sourceVertex.id),
                'target': str(edge.targetVertex.id),
                'weight': str(edge.weight)
            }
            
            # Adiciona label se existir
            if hasattr(edge, 'label') and edge.label:
                edge_attrs['label'] = str(edge.label)
            
            SubElement(edges, 'edge', edge_attrs)

        # Formatação do XML (corrigindo a indentação)
        rough_string = tostring(root, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="  ")
        
        # Remove linhas em branco extras
        pretty_xml = '\n'.join([line for line in pretty_xml.split('\n') if line.strip()])

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(pretty_xml)

        print(f"Grafo exportado como '{filename}'")