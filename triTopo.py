#!/usr/bin/env python3
import random
import networkx as nx

#Algo Kahn : G graphe orienté et sans cycle
def algoKahn(G):
    nodeDegree = {}
    file = []
    ordre = []
    for node in G.nodes:
        nodeDegree[node] = G.in_degree(node)
    for node in nodeDegree:
        if nodeDegree[node] == 0:
            file.append(node)
    while file:
        u = random.choice(file)
        file.remove(u)
        ordre.append(u)

        for v in G.successors(u):
            nodeDegree[v] -= 1
            if nodeDegree[v] == 0:
                file.append(v)
    return ordre

G = nx.DiGraph()
G.add_edges_from([
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3)
])
print(algoKahn(G))