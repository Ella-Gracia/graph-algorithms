#!/usr/bin/env python3
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def graphe():
    G = nx.DiGraph()
    G.add_edges_from([
        (0,1),
        (1,2),
        (2,0),
        (2,3),
        (3,4)
    ])
    # n = int(input('enter the number of nodes: '))
    # G = nx.DiGraph()
    # for i in range(n):
    #     G.add_node(i)
    # for u in G.nodes:
    #     for v in G.nodes:
    #         if u != v:
    #             G.add_edge(u,v)

    nx.draw(G, with_labels=True, arrows=True)
    plt.show()
    return G

def parcours(G, x, pile, retour, dansPile, numEmp, num, partition):
    numEmp[x] = num[0]
    retour[x] = num[0]
    num[0] += 1
    pile.append(x)
    dansPile[x] = True
    for y in G.successors(x): 
        if numEmp[y] == float('inf'):
            parcours(G, y, pile, retour, dansPile, numEmp, num, partition)
            retour[x] = min(retour[x], retour[y])
        else:
            if dansPile[y]:
                retour[x] = min(retour[x], numEmp[y])

    if retour[x] == numEmp[x]:
        while True:
            y = pile[-1]        
            partition[y] = x
            dansPile[y] = False
            pile.pop()           
            if y == x:
                break

def tarjan(G):
    pile = deque()
    retour = {}
    dansPile = {}
    numEmp = {}
    partition = {}

    # initialisation
    for x in G.nodes:
        retour[x] = float('inf')
        numEmp[x] = float('inf')
        dansPile[x] = False
    #récursivité
    num = [0]
    for x in G.nodes:
        if numEmp[x] == float('inf'):
            parcours(G, x, pile, retour, dansPile, numEmp, num, partition)
    return partition

def main(G):
    print(tarjan(G))
    partition= tarjan(G)
    for i in partition:
        if partition[i] == 0:
            print(i)
G = graphe()
main(G)