from collections import deque

my, mx = map(int, input().split())
arr = []
for _ in range(mx) : 
  arr.append(list(map(int,input().split())))

# N, E, S, W
vectors = ((-1,0), (0,1), (1,0), (0,-1))


def bfs(arr) :
  queue = deque()
  cnt = 0
  z_cnt = 0

  # 토마토 탐색 (1. 익은 토마토 위치 / 2. 안익은 토마토 개수)
  for x, row in enumerate(arr) :
    for y, val in enumerate(row) : 
      if val == 1 :
        queue.append(((x,y),0)) # 토마토 좌표, level
      elif val == 0 : 
        z_cnt += 1
  
  while(queue) : 
    [cx,cy], level = queue.popleft()
    # 익은 토마토 기준, 4방향 탐색
    for vector in vectors :
      nx = cx + vector[0]
      ny = cy + vector[1]

      if 0 <= nx < mx and 0 <= ny < my:
        if not arr[nx][ny] : 
          arr[nx][ny] = 1
          z_cnt -= 1
          queue.append(((nx,ny), level+1))

    # 큐가 비워질때마다 cnt 갱신
    if len(queue) == 0 : 
      cnt = level

  # 안익은 토마토 존재 시
  if z_cnt > 0 :
    return -1

  return cnt

print(bfs(arr))