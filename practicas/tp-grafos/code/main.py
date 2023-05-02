from grafo import *

vertices = ['A', 'B', 'C', 'D', 'E','F','G','H','I']
edges = [('B','C'),('C','D'),('E','F'),('F','G'),('G','A'),('A','H'),('H','E'),('B','I'),('I','D')]

v2 = ['A','B','C','D','E']
e2 = [('A','B'),('A','C'),('C','D'),('C','E')]

v = ['A', 'B', 'C', 'D']
e = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]


graph2 = createGraph(v2,e2)
graph3 = createGraph(v,e)

print('Aristas:',len(edges))

my_graph = createGraph(vertices,edges)

print(my_graph)

#grafo 2
print(graph2)

print(existPath(graph2,'A','D'))

print(isConnected(my_graph))

print(countEdges(my_graph))

print(convertToDFSTree(graph2,'A'))

print(hasCycleDFS(graph2))

print(countConnections(my_graph))

print(isTree(graph2))

print(isComplete(graph3))

print(countConnections(graph3))

print(convertToBFSTree(graph2,'A'))

print(bestRoad(graph2,'A','E'))
