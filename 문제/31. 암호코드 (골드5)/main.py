n = input()
dp = [0] * (len(n)+1)

dp[0] = 1
if int(n[0]) > 0 : 
  dp[1] = 1
else : 
  print(0)
  exit()

# 2번째 문자부터, i
for i in range(2,len(n)+1) : 
  # n[i-1], n[i-2:i] 이 현재 숫자
  one = int(n[i-1])
  two = int(n[i-2:i])

  if one > 0 : 
    dp[i] += dp[i-1]
  if 10 <= two <= 26 : 
    dp[i] += dp[i-2]

print(dp[-1] % 1000000)