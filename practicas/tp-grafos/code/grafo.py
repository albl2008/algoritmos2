from queue import Queue

def createGraph(vertices,edges):
  Graph = {}
  for vertex in vertices:
    Graph[vertex] = []
  for vertex1, vertex2 in edges:
    Graph[vertex1].append(vertex2)
    Graph[vertex2].append(vertex1)
  return Graph

def createGraphMatrix(vertices,edges):
  n = len(vertices)
  adj_matrix = [[0] * n for _ in range(n)]

  for edge in edges:
    u = vertices.index(edge[0])
    v = vertices.index(edge[1])
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

  return adj_matrix

def existPath(Grafo, v1, v2):
    visited = set()
    stack = [v1]
    while stack:
      vertex = stack.pop()
      if vertex == v2:
        return True
      if vertex not in visited:
        visited.add(vertex)
        stack.extend(Grafo[vertex])
    return False


def isConnected(Grafo):
  vertices = list(Grafo.keys()) 
  for i in range(len(vertices)):
    v1 = vertices[i]
    for j in range(i+1,len(vertices)):
      v2 = vertices[j]
      flag = existPath(Grafo,v1,v2)
      if flag == False:
        return False

  return True

def countEdges(Grafo):
  contEdges = 0
  for vertex in Grafo:
    contEdges += len(Grafo[vertex])
  return contEdges // 2

def isComplete(Grafo):
    n = len(Grafo)
    for vertex in Grafo:
        if len(Grafo[vertex]) != n-1:
            return False
    return True


def convertToDFSTree(Grafo,v):
  DFS_Tree = {v:[]}
  visited = set()
  DFS(Grafo,v,v,DFS_Tree,visited)
  for vertex in Grafo:
    if vertex not in visited:
      DFS_Tree[vertex]=[]
      DFS(Grafo,vertex,vertex,DFS_Tree,visited)
  return DFS_Tree


def DFS(Grafo,v,root,DFS_Tree,visited):
  visited.add(v)
  for adj_vertex in Grafo[v]:
    if adj_vertex not in visited:
      DFS_Tree[root].append(adj_vertex)
      DFS_Tree[adj_vertex]=[]
      DFS(Grafo,adj_vertex,root,DFS_Tree,visited)


def hasCycleDFS(Grafo):
    visited = set()
    stack = []
    for vertex in Grafo:
      if vertex not in visited:
        stack.append((vertex, None))
        while stack:
          curr, prev = stack.pop()
          visited.add(curr)
          for neighbor in Grafo[curr]:
            if neighbor not in visited:
              stack.append((neighbor, curr))
            elif neighbor != prev:
              return True
    return False

def isTree(Grafo):
  n = len(Grafo)
  edges = countEdges(Grafo)
  if isConnected(Grafo) and hasCycleDFS(Grafo) == False and edges == n-1:
    return True
  else:
    return False


def countConnections(Grafo):
    visited = set()
    count = 0
    for vertex in Grafo:
        if vertex not in visited:
            DFS_2(Grafo, vertex, visited)
            count += 1
    return count

def DFS_2(Grafo, vertex, visited):
    visited.add(vertex)
    for adj_vertex in Grafo[vertex]:
        if adj_vertex not in visited:
            DFS_2(Grafo, adj_vertex, visited)


def convertToBFSTree(Grafo, v):
  visited = set()
  q = Queue()
  visited.add(v)
  q.put(v)
  bfs = {v: []}
  while not q.empty():
    vertex = q.get()
    for neighbor in Grafo[vertex]:
      if neighbor not in visited:
        visited.add(neighbor)
        q.put(neighbor)
        bfs[vertex].append(neighbor)
        bfs[neighbor] = []
  return bfs

def bestRoad(Grafo, v1,v2):
  visited = set()
  q = Queue()
  visited.add(v1)
  q.put((v1, []))
    
  while not q.empty():
    vertex, ruta = q.get()
    if vertex == v2:
      return ruta + [vertex]
    for neighbor in Grafo[vertex]:
      if neighbor not in visited:
        visited.add(neighbor)
        q.put((neighbor, ruta + [vertex]))  
  return [] 

def PRIM(Grafo):
  n = len(Grafo) 
  visitados = [False] * n 
  padre = [None] * n  
  costo = [float('inf')] * n  
  costo[0] = 0
    
  for _ in range(n):
    u = None
    for i in range(n):
      if not visitados[i] and (u is None or costo[i] < costo[u]):
        u = i
    
    visitados[u] = True 
    for v in range(n):
      if Grafo[u][v] != 0 and not visitados[v] and Grafo[u][v] < costo[v]:
        costo[v] = Grafo[u][v]
        padre[v] = u
    
  arbol = [[] for _ in range(n)]
  for v in range(1, n):
    arbol[padre[v]].append(v)
    arbol[v].append(padre[v])
    
  return arbol

def get_peso(arista):
  return arista[2]

def KRUSKAL(Grafo):
  n = len(Grafo)
  aristas = []
  for i in range(n):
    for j in range(i+1, n):
      if Grafo[i][j] != 0:
        aristas.append((i, j, Grafo[i][j]))
  aristas = sorted(aristas, key=get_peso)
  componentes_conexas = [[i] for i in range(n)]
   
  arbol = []
  for arista in aristas:
    u, v, peso = arista
    componente_u = None
    componente_v = None
    for componente in componentes_conexas:
      if u in componente:
        componente_u = componente
      if v in componente:
        componente_v = componente
    if componente_u != componente_v:
      arbol.append((u, v))
      componente_u.extend(componente_v)
      componentes_conexas.remove(componente_v)
  return arbol

