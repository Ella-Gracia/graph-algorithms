#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt

S = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

M = [ [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
      [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
      [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
]

def seachVoisins():
    marque = []
    marque.append(S[0])
    for i in range(10):
        print(f"Les voisins de {S[i]}: ", end= " ")
        for j in range(10):
            if M[i][j] == 1 or M[j][i] == 1:
                print(S[j], end=" ")
        print(" ")
    for i in range(10):
        for j in range(10):
            if (M[i][j] == 1 or M[j][i]) and S[j] not in marque:
                marque.append(S[j])
                i = j
                break
    print(marque, end=" ")
    print(" ")

seachVoisins()
G = nx.Graph()

G.add_node('A')
G.add_nodes_from(['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])

for i in range(10):
    for j in range(10):
        if M[i][j] == 1 or M[j][i] == 1:
            G.add_edge(S[i], S[j])
"""
pos_fixe = {
    'A': (0, 0),
    'B': (1, 0),
    'C': (1, 1)
}
"""
#pos = nx.spring_layout(G, pos=pos_fixe, fixed=pos_fixe.keys())

nx.draw(G, with_labels=True, node_color="red")
plt.show()

# def detectionClique(G):
#     nodes = list(G.nodes)
#     marque = set()
#     clique = []
#     voisins = set()
#     visite = set()

#     depart = random.choice(nodes)
#     marque.add(depart)
#     condition = depart not in clique
#     print(condition)
#     while condition:
#         visite.add(depart)
#         for voisin in G.adj[depart]:
#             voisins.add(voisin)
#         for v in voisins:
#             for v_voisin in G.adj[v]:
#                 visite.add(v_voisin)
#                 if v_voisin in voisins:
#                     marque.add(v_voisin)
#                 else:
#                     continue
#         if len(marque) >= 3:    
#             clique.append(marque)
#         depart = random.choice(list(voisins))

#     print(f"depart: {depart}")
#     print(f"les voisins : {voisins}")
#     print(f"les noeuds visites: {visite}")
#     print(f"Membres de clique: {clique}")

#     return clique

"""
def detectionConnexivite(G):
    #detection sous graphe fortement connexes
    nodes = list(G.nodes)
    depart = random.choice(nodes)
    marque = []
    marque.append(depart)
    for node in G.nodes:
        if G.has_edge(depart,node) and node not in marque:
            print(f"Node : {node}")
            marque.append(node)
            depart = node
    print(f"liste fortement connexe avec {depart}: {marque}")
    print(" ")

"""