#!/usr/bin/env python3
import networkx as nx

def bellmanFord(G, source):
    distance = {v: float('inf') for v in G.nodes}
    distance[source] = 0
    precedent = {}

    for _ in range(len(G.nodes) - 1):
        for u, v, data in G.edges(data=True):
            poids = data['weight']
            if distance[u] + poids < distance[v]:
                distance[v] = distance[u] + poids
                precedent[v] = u

    # détection cycle négatif
    for u, v, data in G.edges(data=True):
        poids = data['weight']
        if distance[u] + poids < distance[v]:
            raise ValueError("Cycle négatif détecté")

    return distance, precedent

print("--- TEST 1 : Poids négatifs sans cycle ---")
G1 = nx.DiGraph()
G1.add_weighted_edges_from([
    ('A', 'B', 6),
    ('A', 'C', 7),
    ('B', 'C', 8),
    ('B', 'D', -4),  
    ('C', 'D', 9),
    ('C', 'E', -3),  
    ('D', 'B', 7),
    ('E', 'D', 7)
])
distances, precedents = bellmanFord(G1, source='A')

print("Distances minimales depuis A :")
for noeud, dist in sorted(distances.items()):
    print(f"Vers {noeud} : {dist}")
