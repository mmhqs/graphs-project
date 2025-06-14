# Biblioteca de Grafos

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

Uma biblioteca Python para manipulação de grafos, com suporte para grafos direcionados e não direcionados, implementados tanto com matriz de adjacência quanto com lista de adjacência.

## Instalação

### Como biblioteca

```bash
pip install git+https://github.com/robertasophia/graphs-project.git
```

### Como programa executável

```bash
# Clone o repositório
git clone https://github.com/robertasophia/graphs-project.git
cd graphs-project

# Execute diretamente
python -m graphs_project.main
```

## Uso como biblioteca

```python
from graphs_project import MatrixGraph, ListGraph

# Criar um grafo direcionado usando matriz de adjacência
grafo = MatrixGraph(directed=True)

# Adicionar vértices
grafo.add_vertex(Vertex("V1"))
grafo.add_vertex(Vertex("V2"))

# Adicionar arestas
grafo.add_edge()  # Irá solicitar input interativamente
```

## Uso como programa

Execute o programa diretamente:

```bash
python -m graphs_project.main
```

Ou, após instalar com pip:

```bash
graphs-cli
```

O programa irá guiá-lo através de um menu interativo para:
- Criar grafos
- Adicionar/remover vértices e arestas
- Atribuir pesos e rótulos
- Verificar propriedades do grafo
- E muito mais!

## Funcionalidades

- Suporte para grafos direcionados e não direcionados
- Implementação com matriz de adjacência e lista de adjacência
- Adição e remoção de vértices e arestas
- Ponderação e rotulação de vértices e arestas
- Verificação de adjacência e incidência
- Análise de propriedades do grafo

## Features

### Graph Representations

- **Adjacency Matrix**  
  A 2D matrix where cell `[i][j]` represents the presence (and optionally the weight) of an edge between vertices `i` and `j`.

- **Adjacency List**  
  A dictionary-based structure where each vertex maps to a list of adjacent vertices (and optionally the weights or labels of edges).

### Core Functionality

The library supports a range of basic and advanced graph operations:

- **Graph Creation**
  - Create a graph with a user-defined number of vertices

- **Edge Manipulation**
  - Add and remove edges

- **Vertex and Edge Labeling**
  - Assign weights and labels to vertices
  - Assign weights and labels to edges

- **Adjacency Checks**
  - Check adjacency between two vertices
  - Check adjacency between two edges

- **Incidence Checks**
  - Verify if an edge is incident to a vertex


  ### How to run the lib
  `C:\github\graphs-project\src> python -m graphs_project.main`




