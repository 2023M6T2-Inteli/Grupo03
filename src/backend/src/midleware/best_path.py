import networkx as nx
from networkx.algorithms import approximation as approx
from collections import deque

# Definir os nós e as arestas do grafo
nodes = [1,2,3,4,5,6,7,8]
WE = [(1,2,1),(1,3,1),(2,4,1),(3,4,2),(3,5,1),(4,5,4),(5,6,1),(6,7,1),(7,8,1)]

# Criar o grafo
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(WE)

# Função para encontrar o melhor caminho passando por todos os nós
def best_path_all_nodes(graph, source):

    # Encontrar um ciclo hamiltoniano aproximado usando o algoritmo Christofides
    cycle = approx.traveling_salesman_problem(graph)

    # Construir o caminho começando no nó de origem
    path = [source]

    # Adicionar os nós do ciclo após o nó de origem na ordem em que aparecem no ciclo
    for i in range (len(cycle)-cycle.index(source)):
        path.append(cycle[cycle.index(source)+i])

    # Adicionar os nós do ciclo antes do nó de origem na ordem em que aparecem no ciclo
    for i in range (cycle.index(source)+1):
        path.append(cycle[i])

    # Remover qualquer nó duplicado no caminho
    repeated = []
    for i in range (1,len(path)):
        if path[i-1] == path[i]:
            repeated.append(i-1)
    for i in repeated:
        path.pop(i)

    # Transformar a lista em uma deque para otimizar as operações de remoção e adição de elementos
    path = deque(path)

    # Retornar o caminho
    return path

# Função principal que solicita o ponto de início e imprime o caminho
def main():
    print(best_path_all_nodes(G, float(input("ponto de ínicio"))))
    
# Verificar se este arquivo é executado como um programa principal e, se sim, executar a função main()
if __name__=="__main__":
    main()
