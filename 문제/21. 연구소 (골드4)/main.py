from collections import deque
from copy import deepcopy
N , M = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]
result = 0 

# N, E, S, W
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs() :
  queue = deque()
  copied_graph = deepcopy(maps)

  for i in range(N) : 
    for j in range(M) : 
      if copied_graph[i][j] == 2 : 
        queue.append((i,j))

  while queue : 
    x,y = queue.popleft()

    for i in range(4) : 
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and copied_graph[nx][ny] == 0 : 
        copied_graph[nx][ny] = 2
        queue.append((nx,ny))
  
  global result
  count = 0
  for row in copied_graph : 
    count += row.count(0)

  result = max(count,result)
  
def make_wall(count) : 
  if count == 3 : 
    bfs()
    return

  for i in range(N) : 
    for j in range(M) : 
      if maps[i][j] == 0 : 
        maps[i][j] = 1 
        make_wall(count+1)
        maps[i][j] = 0


make_wall(0)
print(result)