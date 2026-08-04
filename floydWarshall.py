#!/usr/bin/env python3
import networkx as nx

def floydWarshall(G):
    sommets = list(G.nodes)
    dist = {
        i: {j: float('inf') for j in sommets}
        for i in sommets
    }
    for v in sommets:
        dist[v][v] = 0
    for u, v, data in G.edges(data=True):
        dist[u][v] = data['weight']
    for k in sommets:
        for i in sommets:
            for j in sommets:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

G = nx.DiGraph()
G.add_weighted_edges_from([
    (0, 1, 5),  
    (0, 3, 10),  
    (1, 2, 3),   
    (2, 3, 1),   
])
resultat = floydWarshall(G)
print("Matrice des plus courts chemins :")
for source in sorted(resultat.keys()):
    print(f"Depuis {source} : {dict(sorted(resultat[source].items()))}")