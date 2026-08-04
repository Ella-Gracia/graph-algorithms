#!/usr/bin/env python3
from grapheConnexe import graphe
import heapq
import random

def prim(G, depart):
    visites = set()
    arbre = []
    cout_total = 0
    
    # poids, sommet, parent
    file = [(0, depart, None)]  
    while file:
        poids, u, parent = heapq.heappop(file)
        if u in visites:
            continue
        visites.add(u)
        if parent is not None:
            arbre.append((parent, u, poids))
            cout_total += poids

        for v in G.neighbors(u):
            if v not in visites:
                heapq.heappush(file,(G[u][v]['weight'], v, u))

    return arbre, cout_total

G = graphe()
nodes = list(G.nodes)
# print(nodes)
# print(depart)
depart = random.choice(nodes)
arbre, cout_total = prim(G,depart)
print(f"arbre: {arbre}\ncoût total: {cout_total}")

