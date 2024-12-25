N, K = list(map(int,input().split()))

items = [[0,0]]
for _ in range(N) : 
  items.append(list(map(int,input().split())))

dp = [[0] * (K+1) for i in range(N+1)]

for row in range(1,N+1) : 
  w, v = items[row]

  for col in range(1,K+1) : 
    if col - w >= 0 : 
      dp[row][col] = max(dp[row-1][col], dp[row-1][col-w] + v)
    else : 
      dp[row][col] = dp[row-1][col]

print(dp[-1][-1])
  