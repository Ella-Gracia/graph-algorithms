// BFS (Parcours en Largeur)
MATCH path = (source:Sommet {id: 'A'})-[:SUCC*]->(node:Sommet)
WITH node, length(path) AS niveau
ORDER BY niveau ASC
RETURN DISTINCT node.id AS Ordre_BFS;


// DFS (Parcours en Profondeur)
MATCH path = (source:Sommet {id: 'A'})-[:SUCC*]->(node:Sommet)
WITH node, length(path) AS niveau
ORDER BY niveau DESC
RETURN DISTINCT node.id AS Ordre_DFS;

//  DIJKSTRA / TOPO_DAG (Plus court chemin)
MATCH path = (source:Sommet {id: 'A'})-[:SUCC*]->(destination:Sommet {id: 'F'})
WITH path, reduce(total = 0, r IN relationships(path) | total + r.cout) AS DistanceTotale
RETURN [n IN nodes(path) | n.id] AS Chemin, DistanceTotale
ORDER BY DistanceTotale ASC
LIMIT 1;


// BELLMAN-FORD (Plus court chemin avec détection de boucle)
MATCH path = (source:Sommet {id: 'A'})-[:SUCC*]->(destination:Sommet)
WITH destination, path, reduce(total = 0, r IN relationships(path) | total + r.cout) AS DistanceTotale
ORDER BY DistanceTotale ASC
RETURN destination.id AS Destination, min(DistanceTotale) AS DistanceMinimale;


// KRUSKAL / PRIM (Arbre Couvrant Minimum / MST)
MATCH (u:Sommet)-[r:SUCC]->(v:Sommet)
WITH u, v, r ORDER BY r.cout ASC
RETURN u.id AS Depart, v.id AS Arrivee, r.cout AS Cout_Arete;
