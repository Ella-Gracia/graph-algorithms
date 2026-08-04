#!/usr/bin/env python3
import networkx as nx
from collections import deque
from algoTarjan import parcours , graphe

def algoTarjan2(G):
    partition = {}
    num = [1]
    pile = deque()
    retour = {}
    dansPile = {}
    numEmp = {}

    for x in G.nodes:
        dansPile[x]=False
        numEmp[x]=float('inf')
    for x in G.nodes:
        if numEmp[x] == float('inf'):
            parcours(G, x, pile, retour, dansPile, numEmp, num, partition)
    
    return partition

G = graphe()
print(algoTarjan2(G))