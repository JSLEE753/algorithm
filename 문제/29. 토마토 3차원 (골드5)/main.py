from collections import deque

my, mx, mz = list(map(int, input().split()))

# arr[z][x][y]
arr = []

for z in range(mz) :
  arr.append([])
  for x in range(mx) : 
    arr[z].append(list(map(int,input().split())))


# z+, z-, x+, x-, y+, y-
vectors = ((1,0,0), (-1,0,0) , (0,1,0), (0,-1,0) , (0,0,1) , (0,0,-1))

def bfs() : 
  cnt = 0 
  zero_cnt = 0
  queue = deque()
  for z, h in enumerate(arr) : 
    for x, row in enumerate(h) :
      for y, val in enumerate(row) :
        if val == 1 : 
          queue.append((z,x,y,0))
        elif val == 0 :
          zero_cnt += 1

  while queue : 
    z, x , y, q_cnt = queue.popleft()

    for vector in vectors : 
      nz = z + vector[0]
      nx = x + vector[1]
      ny = y + vector[2]

      if 0 <= nz < mz and 0 <= nx < mx and 0 <= ny < my : 
        if arr[nz][nx][ny] == 0 : 
          arr[nz][nx][ny] = 1
          zero_cnt -= 1
          queue.append((nz,nx,ny,q_cnt+1))
    
    cnt = q_cnt
    

  if zero_cnt > 0 : 
    return -1
  
  return cnt


print(bfs())