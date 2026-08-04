#!/usr/bin/env python3
import networkx as nx
import matplotlib.pyplot as plt
sommets = ['A','B','C','D','E','F','G']
color = 'white'

def chemin(qInit, qS):
    if qInit == qS:
        return True
    color = 'black'
    for v in sommets:
        if color == 'white':
            qInit = v
            trouve = chemin(qInit, qS)
            if trouve:
                return True
    return False

qInit = sommets[0]
for v in sommets:
    chemin(qInit,v)
