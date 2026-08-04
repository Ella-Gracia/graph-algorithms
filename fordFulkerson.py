#!/usr/bin/env python3
from collections import deque

def bfs(capacite, source, puits, parent):
    visites = set([source])
    file = deque([source])
    while file:
        u = file.popleft()
        for v in capacite[u]:
            if v not in visites and capacite[u][v] > 0:
                visites.add(v)
                parent[v] = u
                if v == puits:
                    return True
                file.append(v)

    return False

def fordFulkerson(capacite, source, puits):
    parent = {}
    flot_max = 0
    while bfs(capacite, source, puits, parent):
        flot = float('inf')
        s = puits
        while s != source:
            flot = min(flot, capacite[parent[s]][s])
            s = parent[s]
        flot_max += flot
        v = puits
        while v != source:
            u = parent[v]
            capacite[u][v] -= flot
            capacite[v][u] += flot
            v = u

    return flot_max

graph = {
    0: {1: 16, 2: 13, 3: 0,  4: 0,  5: 0},  
    1: {0: 0,  2: 10, 3: 12, 4: 0,  5: 0},
    2: {0: 0,  1: 4,  3: 0,  4: 14, 5: 0},
    3: {0: 0,  1: 0,  2: 9,  4: 0,  5: 20},
    4: {0: 0,  1: 0,  2: 0,  3: 7,  5: 4},
    5: {0: 0,  1: 0,  2: 0,  3: 0,  4: 0}   
}
resultat = fordFulkerson(graph, source=0, puits=5)
print("Le flot maximum trouvé est :", resultat)