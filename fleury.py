#!/usr/bin/env python3
import networkx as nx
def fleury(G, depart):
    chemin = [depart]
    u = depart
    while G.number_of_edges() > 0:
        voisins = list(G.neighbors(u))
        for v in voisins:
            if len(voisins) == 1:
                choisi = v
                break
            G.remove_edge(u, v)
            if nx.is_connected(G):
                choisi = v
                G.add_edge(u, v)
                break
            G.add_edge(u, v)
        G.remove_edge(u, choisi)
        chemin.append(choisi)
        u = choisi
    return chemin
G = nx.Graph()
G.add_edges_from([
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0)
])
G_test = G.copy()
resultat = fleury(G_test, depart=0)
print("Cycle eulérien à 5 nœuds :", resultat)