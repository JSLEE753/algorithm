from collections import deque

# 데이터 생성
N, L, R = map(int, input().split())
ctrs = [list(map(int, input().split())) for _ in range(N)]

# NESW
vectors = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(ctrs, visited, i, j):
  queue = deque([(i, j)])
  visited[i][j] = 1
  adj = [(i, j)]
  acc = ctrs[i][j] # 누적 인구. 초기값은 선택된 도시의 인구.

  while queue:
    x, y = queue.popleft()

    for dx, dy in vectors:
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        if L <= abs(ctrs[x][y] - ctrs[nx][ny]) <= R:
          queue.append((nx, ny))
          visited[nx][ny] = 1
          adj.append((nx, ny))
          acc += ctrs[nx][ny]

  return adj, acc // len(adj) if adj else ctrs[i][j]

n = 0
while True:
  visited = [[0] * N for _ in range(N)] # 매 반복마다 새로운 visited 사용
  flag = False  # 인구 이동이 있었는가
  for i in range(N):
    for j in range(N):
      if not visited[i][j]:  
        adj, acc = bfs(ctrs, visited, i, j)
        if len(adj) > 1:  # 연합이 존재할 때만 인구 이동
          for x, y in adj:
            ctrs[x][y] = acc
          flag = True

  if not flag:  
    break
  n += 1

print(n)
