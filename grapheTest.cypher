// 1. Nettoyage
MATCH (n) DETACH DELETE n;

// 2. Sommets
CREATE (a:Sommet {id: 'A'}), (b:Sommet {id: 'B'}), (c:Sommet {id: 'C'}), 
       (d:Sommet {id: 'D'}), (e:Sommet {id: 'E'}), (f:Sommet {id: 'F'});

// 3. Arêtes (Utilisées pour tous les algorithmes)
MATCH (a:Sommet {id:'A'}), (b:Sommet {id:'B'}), (c:Sommet {id:'C'}), (d:Sommet {id:'D'}), (e:Sommet {id:'E'}), (f:Sommet {id:'F'})
CREATE (a)-[:SUCC {cout: 4}]->(b),
       (a)-[:SUCC {cout: 2}]->(c),
       (c)-[:SUCC {cout: 1}]->(b),
       (b)-[:SUCC {cout: 5}]->(d),
       (c)-[:SUCC {cout: 8}]->(e),
       (d)-[:SUCC {cout: 2}]->(e),
       (d)-[:SUCC {cout: 6}]->(f),
       (e)-[:SUCC {cout: 3}]->(f);
