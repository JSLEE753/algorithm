N, K = list(map(int,input().split()))
dp = [[_] * (N+1) for _ in range(K+1)]
dp[1] = [1] * (N+1)

if K > 1 :
  dp[2] = [a+1 for a in range(N+1)]


for i in range(3,K+1) : 
  for j in range(2,N+1) : 
    dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1] % 1000000000)

