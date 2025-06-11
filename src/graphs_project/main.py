
from graphs_project.matrix import MatrixGraph
from graphs_project.vertex import Vertex


def create_graph():
    print("Olá, pessoa! Bem-vindo(a) à nossa biblioteca de grafos.\n")

    # Grafo direcionado ou não direcionado?
    while True:
        print("Seu grafo é:")
        print("1 - 🎯 Direcionado")
        print("2 - 🔁 Não direcionado")
        tipo = input("Escolha (1 ou 2): ")

        if tipo == "1":
            directed = True
            break
        elif tipo == "2":
            directed = False
            break
        else:
            print("Opção inválida. Tente novamente.\n")

    # Matriz ou lista de adjacência?
    while True:
        print("\nVocê quer criar um grafo a partir de:")
        print("1 - 🎲 Matriz de adjacência")
        print("2 - 📋 Lista de adjacência")
        escolha = input("Escolha (1 ou 2): ")

        if escolha == "1":
            graph = MatrixGraph(directed)
            break
        elif escolha == "2":
            print(
                "ListGraph ainda não implementado. Usando MatrixGraph como fallback.")
            graph = MatrixGraph(directed)
            break
        else:
            print("Opção inválida. Tente novamente.\n")

    return graph


def menu(graph):
    while True:
        print("\nMenu:")
        print("1 - ➕ Adicionar vértices")
        print("2 - 🔗 Adicionar aresta")
        print("3 - ❌ Remover aresta")
        print("4 - 🧮 Exibir matriz de adjacência")
        print("5 - ⚖️ Atribuir peso a um vértice")
        print("6 - 🏷️ Rotular um vértice")
        print("7 - ⚖️ Atribuir peso a uma aresta")
        print("8 - 🏷️ Rotular uma aresta")
        print("0 - 🚪 Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            graph.add_vertices()
        elif opcao == "2":
            graph.add_edge()
        elif opcao == "3":
            graph.remove_edge()
        elif opcao == "4":
            graph.display()
        elif opcao == "5":
            graph.set_vertex_weight()
        elif opcao == "6":
            graph.set_vertex_label()
        elif opcao == "7":
            graph.set_edge_weight()
        elif opcao == "8":
            graph.set_edge_label()
        elif opcao == "0":
            print("Saindo. Obrigado por usar a biblioteca de grafos!")
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    grafo = create_graph()
    menu(grafo)


if __name__ == "__main__":
    main()
