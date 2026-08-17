#!/usr/bin/env python3
def triTopologique(graphe):
    visite = set()
    ordre = []
    def dfs(sommet):
        if sommet not in visite:
            visite.add(sommet)
            for voisin in graphe.get(sommet, {}):
                dfs(voisin)
            ordre.append(sommet)

    for sommet in graphe:
        dfs(sommet)
    return ordre[::-1] 

def relacher(si, sj, cout_arete, d, pi):
    if d[sj] > d[si] + cout_arete:
        d[sj] = d[si] + cout_arete
        pi[sj] = si

def topo_dag(graphe, s0):
    d = {sommet: float('inf') for sommet in graphe}
    pi = {sommet: None for sommet in graphe}
    
    d[s0] = 0 
    ordre_topologique = triTopologique(graphe)

    for si in ordre_topologique:
        if d[si] == float('inf'): 
            continue 
        for sj, cout_arete in graphe.get(si, {}).items():
            relacher(si, sj, cout_arete, d, pi)
            
    return pi, d
mon_dag = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'E': 3},
    'D': {'E': 1},
    'E': {}
}
predecesseurs, distances = topo_dag(mon_dag, 'A')
print("Distances depuis A:", distances)
print("Prédécesseurs:", predecesseurs)
