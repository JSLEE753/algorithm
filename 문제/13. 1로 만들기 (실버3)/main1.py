from collections import deque

n = int(input())

def f(n) : 
  queue = deque([])
  level = 0

  queue.append((n,level))

  while(queue) :
    new_n, new_level = queue.popleft()
    if new_n == 1 : 
      level = new_level
      break

    if new_n % 3 == 0 :
      queue.append((new_n//3, new_level + 1))
    if new_n % 2 == 0 :
      queue.append((new_n//2, new_level + 1))

    queue.append((new_n-1, new_level+1))
    
  return level
    
print(f(n))


###

def f(n):
    dp = [0] * (n + 1)  
    
    for i in range(2, n + 1):  
        dp[i] = dp[i - 1] + 1  
        
        if i % 2 == 0:  
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:  
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]

n = int(input())
print(f(n))