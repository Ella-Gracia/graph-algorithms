#!/usr/bin/env python3
from grapheConnexe import graphe

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rang, x, y):
    racineX = find(parent, x)
    racineY = find(parent, y)
    if racineX == racineY:
        return
    # union par rang
    if rang[racineX] < rang[racineY]:
        parent[racineX] = racineY
    elif rang[racineX] > rang[racineY]:
        parent[racineY] = racineX
    else:
        parent[racineY] = racineX
        rang[racineX] += 1

def kruskal(G):
    arbre = []
    parent = {}
    rang = {}
    for sommet in G.nodes:
        parent[sommet] = sommet
        rang[sommet] = 0
    aretes = sorted(
        G.edges(data=True),
        key=lambda x: x[2]['weight']
    )
    # parcours des arêtes
    for u, v, data in aretes:
        if find(parent, u) != find(parent, v):
            arbre.append((u, v, data['weight']))
            union(parent, rang, u, v)
    return arbre

G = graphe()
arbre = kruskal(G)
print("Arbre couvrant minimal :")
poids_arbre = 0
for u, v, poids in arbre:
    print(f"{u} -- {v} : poids = {poids}")
    poids_arbre += poids

print("Coût total :", poids_arbre)