n, m, v = map(int,input().split())
raw_graph = []
for i in range(m) : 
  raw_graph.append(list(map(int, input().split())))

graph = [[] for _ in range(n+1)]
for v1, v2 in raw_graph:
    graph[v1].append(v2)
    graph[v2].append(v1)

for idx in range(len(graph)) : 
  graph[idx] = list(set(graph[idx]))

for edges in graph:
    edges.sort()

#################################
# dfs

visited = [0] * (n+1)
dfs_result = ''

def dfs(graph, v, visited) :
  global dfs_result
  dfs_result += str(v) + ' '

  visited[v] = 1
  
  for i in graph[v] :
    if not visited[i] :
      dfs(graph, i , visited) 

dfs(graph,v,visited)
dfs_result = dfs_result.strip()
print(dfs_result)

#################################
# bfs


bfs_result = ''

from collections import deque
visited = [0] * (n+1)
def bfs(graph,v,visited) : 
  global bfs_result
  queue = deque()
  visited[v] = 1
  queue.append(v) 

  while queue : 
    nv = queue.popleft()
    bfs_result += str(nv) + ' '
    for adj in graph[nv] : 
      if not visited[adj] :
        visited[adj] = 1
        queue.append(adj)
      

bfs(graph, v, visited)
bfs_result = bfs_result.strip()
print(bfs_result)
  