
MATCH (source:Sommet {id: 'A'})
CALL apoc.path.expandNodes(source, "SUCC>", "+Sommet", 0, -1) 
YIELD node
RETURN node.id AS Ordre_BFS;

MATCH (source:Sommet {id: 'A'})
CALL apoc.path.expandNodes(source, "SUCC>", "+Sommet", 0, -1, {bfs: false}) 
YIELD node
RETURN node.id AS Ordre_DFS;

MATCH (source:Sommet {id: 'A'}), (destination:Sommet {id: 'F'})
CALL apoc.algo.dijkstra(source, destination, 'SUCC', 'cout') 
YIELD path, weight
RETURN [n IN nodes(path) | n.id] AS Chemin, weight AS DistanceTotale;

// projection du DAG
CALL gds.graph.project('monDAG', 'Sommet', { SUCC: { type: 'SUCC', properties: 'cout' } });

// calcul basé sur le tri topologique
MATCH (source:Sommet {id: 'A'})
CALL gds.shortestPath.dijkstra.stream('monDAG', { sourceNode: source, relationshipWeightProperty: 'cout' })
YIELD nodeIds, costs
RETURN gds.util.asNode(nodeIds[-1]).id AS Destination, costs[-1] AS Distance_Min;

// nettoyage après exécution
CALL gds.graph.drop('monDAG');

CALL gds.graph.project('monGrapheBF', 'Sommet', { SUCC: { type: 'SUCC', properties: 'cout' } });

MATCH (source:Sommet {id: 'A'})
CALL gds.allShortestPaths.delta.stream('monGrapheBF', { sourceNode: source, relationshipWeightProperty: 'cout' })
YIELD targetNode, totalCost
RETURN gds.util.asNode(targetNode).id AS Destination, totalCost AS Distance
ORDER BY Destination;

CALL gds.graph.drop('monGrapheBF');


CALL gds.graph.project('grapheACM', 'Sommet', { LIAISON: { type: 'LIAISON', properties: 'cout', orientation: 'UNDIRECTED' } });

MATCH (source:Sommet {id: 'A'})
CALL gds.spanningTree.minimum.stream('grapheACM', {
  sourceNode: source,
  relationshipWeightProperty: 'cout'
})
YIELD nodeFrom, nodeTo, weight
RETURN gds.util.asNode(nodeFrom).id AS Depart, gds.util.asNode(nodeTo).id AS Arrivee, weight AS Cout_Arete;

CALL gds.graph.drop('grapheACM');
