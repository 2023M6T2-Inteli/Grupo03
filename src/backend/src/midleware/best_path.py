import networkx as nx
import math
from networkx.algorithms import approximation as approx
from collections import deque

def Graph():
    nodes = []
    WE = []
    G = nx.Graph()

    class Position_Node():
        def __init__(self, name, x, y):
            self.name = name
            self.x = x
            self.y = y
            nodes.append(self)

        def __repr__(self):
            return f"node{self.name}"

    def Weighed_Edge(p1, p2):
        weitgh = math.sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))
        weitghEdge = (p1, p2, weitgh)
        WE.append(weitghEdge)
    
    #seting nodes
    i = 1
    vn = []
    while True:
        x = float(input(f"Digite a coordenada x do nó {i}: "))
        y = float(input(f"Digite a coordenada y do nó {i}: "))
        node  = Position_Node(i,x,y)
        vn.append((node.x,node.y))
        i += 1
        end = input("Voce quer adicionar algum nó? (y/n) ")
        if end == 'n' or end == 'N':
            break
        print(vn)

    print(nodes)
    G.add_nodes_from(nodes)

    while True:
        end = input("Voce quer adicionar alguma aresta? (y/n)")
        if end == "n" or end == "N":
            break
        
        p1 = nodes[int(input(f"{vn} De que ponto voce quer adicionar a aresta? Digite a posição do ponto na lista. Considere que o primeiro ponto é o 0.  "))]
        p2 = nodes[int(input(f"{vn} Com qual ponto voce quer conectar o ponto {p1}? Digite a posição do ponto na lista. Considere que o primeiro ponto é o 0.  "))]
        Weighed_Edge(p1, p2)
    
    G.add_weighted_edges_from(WE)
    return (G, vn, nodes)


    


# Função para encontrar o melhor caminho passando por todos os nós
def best_path_all_nodes(graph, source):

    print(source)
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
    G = Graph()
    graph = G[0]
    nodes = G[2]
    p0 = int(input(f"{G[1]} De que ponto voce quer começar o percurso? Digite a posição do ponto na lista. Considere que o primeiro ponto é o 0"))
    print(G)
    print(best_path_all_nodes(graph, nodes[p0]))
    
# Verificar se este arquivo é executado como um programa principal e, se sim, executar a função main()
if __name__=="__main__":
    main()
