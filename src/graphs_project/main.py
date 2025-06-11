
from graphs_project.matrix import MatrixGraph
from graphs_project.vertex import Vertex


def criar_grafo():
    print("Olá, pessoa! Bem-vindo(a) à nossa biblioteca de grafos.\n")

    # Grafo direcionado ou não direcionado?
    while True:
        print("Seu grafo é:")
        print("1 - Direcionado")
        print("2 - Não direcionado")
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
        print("1 - Matriz de adjacência")
        print("2 - Lista de adjacência")
        escolha = input("Escolha (1 ou 2): ")

        if escolha == "1":
            grafo = MatrixGraph(directed)
            break
        elif escolha == "2":
            print(
                "ListGraph ainda não implementado. Usando MatrixGraph como fallback.")
            grafo = MatrixGraph(directed)
            break
        else:
            print("Opção inválida. Tente novamente.\n")

    return grafo


def menu_principal(grafo):
    while True:
        print("\nMenu:")
        print("1 - Adicionar vértices")
        print("2 - Adicionar aresta")
        print("3 - Exibir matriz de adjacência")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            grafo.add_vertices()
        elif opcao == "2":
            v1 = input("ID do vértice de origem: ")
            v2 = input("ID do vértice de destino: ")
            peso = input("Peso (pressione Enter para usar 1): ")
            try:
                peso = float(peso) if peso.strip() != "" else 1
                grafo.add_edge(v1, v2, peso)
            except ValueError:
                print("Peso inválido.")
        elif opcao == "3":
            grafo.display()
        elif opcao == "0":
            print("Saindo. Obrigado por usar a biblioteca de grafos!")
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    grafo = criar_grafo()
    menu_principal(grafo)


if __name__ == "__main__":
    main()
