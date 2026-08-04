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

def parcoursLargeur():
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
                # i = j
                # break
    print(marque, end=" ")
    print(" ")

parcoursLargeur()
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
