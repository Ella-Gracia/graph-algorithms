// Nettoyage de la base de données
MATCH (n) DETACH DELETE n;

// Creation des nœuds
CREATE (a:Sommet {id: 'A'}), (b:Sommet {id: 'B'}), (c:Sommet {id: 'C'}), 
       (d:Sommet {id: 'D'}), (e:Sommet {id: 'E'}), (f:Sommet {id: 'F'});

MATCH (a:Sommet {id:'A'}), (b:Sommet {id:'B'}), (c:Sommet {id:'C'}), (d:Sommet {id:'D'}), (e:Sommet {id:'E'}), (f:Sommet {id:'F'})
CREATE (a)-[:SUCC {cout: 4}]->(b),
       (a)-[:SUCC {cout: 2}]->(c),
       (c)-[:SUCC {cout: 1}]->(b),
       (b)-[:SUCC {cout: 5}]->(d),
       (c)-[:SUCC {cout: 8}]->(e),
       (d)-[:SUCC {cout: 2}]->(e),
       (d)-[:SUCC {cout: 6}]->(f),
       (e)-[:SUCC {cout: 3}]->(f);

MATCH (a:Sommet {id:'A'}), (b:Sommet {id:'B'}), (c:Sommet {id:'C'}), (d:Sommet {id:'D'}), (e:Sommet {id:'E'}), (f:Sommet {id:'F'})
CREATE (a)-[:LIAISON {cout: 4}]->(b),
       (a)-[:LIAISON {cout: 2}]->(c),
       (c)-[:LIAISON {cout: 1}]->(b),
       (b)-[:LIAISON {cout: 5}]->(d),
       (c)-[:LIAISON {cout: 8}]->(e),
       (d)-[:LIAISON {cout: 2}]->(e),
       (d)-[:LIAISON {cout: 6}]->(f),
       (e)-[:LIAISON {cout: 3}]->(f);
