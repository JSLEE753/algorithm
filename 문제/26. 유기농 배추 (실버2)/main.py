import sys
sys.setrecursionlimit(10**6)

# N E S W
vectors = [(-1,0), (0,1), (1,0), (0,-1)]

def dfs(test_case, len_x, len_y, x , y) : 
  if test_case[x][y][0] == 1 and test_case[x][y][1] == 0 : 
    test_case[x][y][1] = 1
    for i in range(4) : 
      nx = x + vectors[i][0]
      ny = y + vectors[i][1]

      if 0 <= nx < len_x and 0 <= ny < len_y and test_case[nx][ny][1] == 0 : 
        dfs(test_case, len_x, len_y, nx , ny)
    return True
  return False

tc = int(input()) # test case 개수
cnt = [0] * tc
test_cases = []

for i in range(tc) : 
  #가로, 세로, 배추 개수
  xn, yn, cn = map(int,input().split())
  # [ 배추유무 , visited ]
  arr = [[[0, 1] for _ in range(yn)] for _ in range(xn)]
  
  for i in range(cn) :
    x , y = map(int,input().split())  
    arr[x][y] = [1,0]
  test_cases.append(arr)

for idx, test_case in enumerate(test_cases) : 
  len_x = len(test_case)
  len_y = len(test_case[0])

  for x, row in enumerate(test_case) :
    for y, col in enumerate(row) :
        if (test_case[x][y][1] == 0 and dfs(test_case, len_x, len_y, x , y)) :
          cnt[idx] += 1

for i in cnt :
  print(i)