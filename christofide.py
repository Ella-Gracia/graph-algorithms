#!/usr/bin/env python3
import networkx as nx

def christofides(G):
    T = nx.minimum_spanning_tree(G)
    impairs = [v for v in T.nodes if T.degree(v) % 2 == 1]
    sous_graphe = G.subgraph(impairs)
    couplage = nx.min_weight_matching(
        sous_graphe,
        weight='weight'
    )
    multigraphe = nx.MultiGraph(T)
    for u, v in couplage:
        multigraphe.add_edge(
            u, v,
            weight=G[u][v]['weight']
        )

    cycle = list(nx.eulerian_circuit(multigraphe))
    parcours = []
    visites = set()
    for u, _ in cycle:
        if u not in visites:
            visites.add(u)
            parcours.append(u)
    parcours.append(parcours[0])

    return parcours

G = nx.Graph()
G.add_weighted_edges_from([
    ('A', 'B', 10), ('A', 'C', 15), ('A', 'D', 20),
    ('B', 'C', 35), ('B', 'D', 25),
    ('C', 'D', 30)
])
tour = christofides(G)
cout_total = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

print("Tournée du voyageur de commerce :", tour)
print("Coût total du parcours :", cout_total)