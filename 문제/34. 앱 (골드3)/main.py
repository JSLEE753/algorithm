N, threshold = list(map(int,input().split()))
memories = list(map(int,input().split()))
costs = list(map(int,input().split()))

items = [[0,0]]
for i in range(N) : 
  items.append([costs[i], memories[i]])

cost_sum = sum(costs)

dp = [[0] * (cost_sum + 1) for _ in range(len(items) + 1)]

min_cost = 100 * 100 + 1

for row in range(1,N+1) :
  cost = items[row][0]
  memory = items[row][1]
  for col in range(0,cost_sum + 1) :

    if col >= cost :
      dp[row][col] = max(dp[row-1][col-cost] + memory, dp[row-1][col])
    else : 
      dp[row][col] = dp[row-1][col]


    if dp[row][col] >= threshold : 
      min_cost = min(min_cost, col)

print(min_cost)