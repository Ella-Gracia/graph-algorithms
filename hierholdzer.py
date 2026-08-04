#!/usr/bin/env python3
import networkx as nx

def hierholzer(G, depart):
    pile = [depart]
    cycle = []
    while pile:
        u = pile[-1]
        if G.degree(u) == 0:
            cycle.append(pile.pop())
        else:
            v = next(iter(G.neighbors(u)))
            G.remove_edge(u, v)
            pile.append(v)
    return cycle[::-1]

G = nx.Graph()
G.add_edges_from([
    (0, 1), (1, 2), (2, 0),  
    (2, 3), (3, 4), (4, 2)  
])
G_test = G.copy()
resultat = hierholzer(G_test, depart=0)
print("Cycle eulérien trouvé :", resultat)
