# Biblioteca de Grafos

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

Esta biblioteca oferece duas implementações diferentes de grafos: usando Matriz de Adjacência (`MatrixGraph`) e Lista de Adjacência (`ListGraph`). Pode ser utilizada tanto como uma biblioteca Python quanto como um programa interativo via linha de comando.

## Índice

1. [Instalação](#instalação)
2. [Uso como Programa](#uso-como-programa)
3. [Uso como Biblioteca](#uso-como-biblioteca)
4. [Documentação da API](#documentação-da-api)
5. [Exemplos](#exemplos)

## Instalação

### Como biblioteca

```bash
pip install git+https://github.com/mmhqs/graphs-project.git
```

### Para desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/mmhqs/graphs-project.git
cd graphs-project

# Execute diretamente
python -m graphs_project.main
```

## Uso como Programa

O projeto pode ser executado como um programa interativo de duas formas:

### 1. Após instalar com pip:

```bash
graphs-cli
```

### 2. Executando diretamente do código fonte:

```bash
python -m graphs_project.main
```

O programa oferece um menu interativo com as seguintes opções:

1. **Criar Grafo**
   - Escolher entre matriz ou lista de adjacência
   - Definir se é direcionado ou não

2. **Manipular Vértices**
   - Adicionar vértices
   - Definir pesos
   - Definir rótulos

3. **Manipular Arestas**
   - Adicionar arestas
   - Remover arestas
   - Modificar pesos e rótulos

4. **Consultas e Verificações**
   - Verificar adjacência entre vértices
   - Verificar adjacência entre arestas
   - Verificar incidência
   - Consultar quantidade de vértices e arestas
   - Verificar se o grafo é vazio ou completo

## Uso como Biblioteca

Para usar como biblioteca, importe as classes necessárias:

```python
from graphs_project.matrix import MatrixGraph
from graphs_project.list import ListGraph
```

### Conceitos Básicos

A biblioteca implementa grafos com as seguintes características:

- **Vértices**: Podem ter peso e rótulo
- **Arestas**: Podem ter peso e rótulo
- **Direcionamento**: Os grafos podem ser direcionados ou não-direcionados
- **Duas Implementações**: 
  - `MatrixGraph`: Usa matriz de adjacência (melhor para grafos densos)
  - `ListGraph`: Usa lista de adjacência (melhor para grafos esparsos)

### Uso Básico

#### 1. Criando um Grafo

```python
# Grafo não direcionado (padrão)
graph = MatrixGraph()  # ou ListGraph()

# Grafo direcionado
graph_dir = MatrixGraph(directed=True)  # ou ListGraph(directed=True)
```

#### 2. Manipulando Vértices

```python
# Adicionando um único vértice
vertex = graph.lib_add_vertex("A")

# Adicionando múltiplos vértices (V0, V1, V2, ...)
vertices = graph.lib_add_vertices(3)  # Cria 3 vértices: V0, V1, V2

# Definindo peso de um vértice
graph.lib_set_vertex_weight("A", 10.5)

# Definindo rótulo de um vértice
graph.lib_set_vertex_label("A", "Início")
```

#### 3. Manipulando Arestas

```python
# Adicionando uma aresta
edge = graph.lib_add_edge(
    source_id="A",
    target_id="B",
    weight=2.5,
    label="Conexão A-B"
)

# Removendo uma aresta (por vértices)
graph.lib_remove_edge(source_id="A", target_id="B")

# Removendo uma aresta (por rótulo)
graph.lib_remove_edge(label="Conexão A-B")

# Modificando peso de uma aresta
graph.lib_set_edge_weight(
    weight=3.0,
    source_id="A",
    target_id="B"
)

# Modificando rótulo de uma aresta
graph.lib_set_edge_label(
    new_label="Nova Conexão",
    source_id="A",
    target_id="B"
)
```

## Documentação da API

### Classe MatrixGraph e ListGraph

Ambas as classes compartilham a mesma interface, diferindo apenas na implementação interna.

#### Métodos para Vértices

1. `lib_add_vertex(vertex_id: str) -> Vertex`
   - Adiciona um vértice ao grafo
   - **Parâmetros**:
     - `vertex_id`: ID único do vértice
   - **Retorna**: O vértice criado
   - **Exceções**: `ValueError` se o vértice já existir

2. `lib_add_vertices(count: int) -> list[Vertex]`
   - Adiciona múltiplos vértices
   - **Parâmetros**:
     - `count`: Número de vértices a criar
   - **Retorna**: Lista dos vértices criados
   - **Exceções**: `ValueError` se count <= 0

3. `lib_set_vertex_weight(vertex_id: str, weight: float) -> Vertex`
   - Define o peso de um vértice
   - **Parâmetros**:
     - `vertex_id`: ID do vértice
     - `weight`: Novo peso
   - **Retorna**: O vértice atualizado
   - **Exceções**: `ValueError` se o vértice não existir

4. `lib_set_vertex_label(vertex_id: str, label: str) -> Vertex`
   - Define o rótulo de um vértice
   - **Parâmetros**:
     - `vertex_id`: ID do vértice
     - `label`: Novo rótulo
   - **Retorna**: O vértice atualizado
   - **Exceções**: `ValueError` se o vértice não existir

#### Métodos para Arestas

1. `lib_add_edge(source_id: str, target_id: str, weight: float = 1, label: str = None) -> Edge`
   - Adiciona uma aresta ao grafo
   - **Parâmetros**:
     - `source_id`: ID do vértice de origem
     - `target_id`: ID do vértice de destino
     - `weight`: Peso da aresta (opcional, padrão = 1)
     - `label`: Rótulo da aresta (opcional)
   - **Retorna**: A aresta criada

2. `lib_remove_edge(source_id: str = None, target_id: str = None, label: str = None) -> Edge`
   - Remove uma aresta do grafo
   - **Parâmetros** (usar ou source_id+target_id OU label):
     - `source_id`: ID do vértice de origem
     - `target_id`: ID do vértice de destino
     - `label`: Rótulo da aresta
   - **Retorna**: A aresta removida
   - **Exceções**: `ValueError` se a aresta não existir

3. `lib_set_edge_weight(weight: float, source_id: str = None, target_id: str = None, label: str = None) -> Edge`
   - Define o peso de uma aresta
   - **Parâmetros**:
     - `weight`: Novo peso
     - `source_id`: ID do vértice de origem (opcional)
     - `target_id`: ID do vértice de destino (opcional)
     - `label`: Rótulo da aresta (opcional)
   - **Retorna**: A aresta atualizada
   - **Exceções**: `ValueError` se a aresta não existir

4. `lib_set_edge_label(new_label: str, source_id: str = None, target_id: str = None, old_label: str = None) -> Edge`
   - Define o rótulo de uma aresta
   - **Parâmetros**:
     - `new_label`: Novo rótulo
     - `source_id`: ID do vértice de origem (opcional)
     - `target_id`: ID do vértice de destino (opcional)
     - `old_label`: Rótulo atual da aresta (opcional)
   - **Retorna**: A aresta atualizada
   - **Exceções**: `ValueError` se a aresta não existir

## Exemplos

### Exemplo 1: Criando um Grafo Simples

```python
from graphs_project.matrix import MatrixGraph

# Cria um grafo não direcionado
graph = MatrixGraph()

# Adiciona vértices
graph.lib_add_vertex("A")
graph.lib_add_vertex("B")
graph.lib_add_vertex("C")

# Adiciona arestas
graph.lib_add_edge("A", "B", weight=2.5, label="AB")
graph.lib_add_edge("B", "C", weight=1.8, label="BC")
graph.lib_add_edge("C", "A", weight=3.0, label="CA")

# Modifica alguns atributos
graph.lib_set_vertex_weight("A", 10)
graph.lib_set_edge_label(new_label="Nova_AB", old_label="AB")
```

### Exemplo 2: Grafo Direcionado com Lista de Adjacência

```python
from graphs_project.list import ListGraph

# Cria um grafo direcionado
graph = ListGraph(directed=True)

# Adiciona vários vértices de uma vez
vertices = graph.lib_add_vertices(5)  # Cria V0, V1, V2, V3, V4

# Cria algumas arestas
graph.lib_add_edge("V0", "V1")
graph.lib_add_edge("V1", "V2")
graph.lib_add_edge("V2", "V3")
graph.lib_add_edge("V3", "V4")
graph.lib_add_edge("V4", "V0")  # Cria um ciclo

# Remove uma aresta
graph.lib_remove_edge(source_id="V4", target_id="V0")
```

### Exemplo 3: Manipulação de Pesos e Rótulos

```python
from graphs_project.matrix import MatrixGraph

graph = MatrixGraph()

# Adiciona vértices com rótulos
graph.lib_add_vertex("Start")
graph.lib_add_vertex("Middle")
graph.lib_add_vertex("End")

# Define pesos para os vértices
graph.lib_set_vertex_weight("Start", 1.0)
graph.lib_set_vertex_weight("Middle", 2.0)
graph.lib_set_vertex_weight("End", 3.0)

# Adiciona arestas com pesos e rótulos
graph.lib_add_edge("Start", "Middle", weight=5.0, label="Início")
graph.lib_add_edge("Middle", "End", weight=5.0, label="Fim")

# Modifica os pesos das arestas
graph.lib_set_edge_weight(10.0, source_id="Start", target_id="Middle")
```

## Funcionalidades

- Suporte para grafos direcionados e não direcionados
- Implementação com matriz de adjacência e lista de adjacência
- Adição e remoção de vértices e arestas
- Ponderação e rotulação de vértices e arestas
- Verificação de adjacência e incidência
- Análise de propriedades do grafo




