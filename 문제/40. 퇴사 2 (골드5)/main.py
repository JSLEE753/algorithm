N = int(input())
days = [[0,0]]
# days = [[금액1, 소요 시간1], [금액2, 소요 시간2],]
for _ in range(N) :
  days.append(list(reversed(list(map(int,input().split())))))

dp = [0] * (N + 1)

for i in range(1, N + 1) : 
  val = days[i][0]
  due = days[i][1]

  # 이전 날짜와 현재 날짜 중 큰 값 선택
  dp[i] = max(dp[i], dp[i - 1])

  # 상담 완료일 = 현재 날짜 + 소요 시간 - 1 
  comp = i + due - 1

  if comp <= N :  
    # ( 이전 날짜의 금액 + 현재 금액 , 이미 적혀있는 완료 날짜의 금액 ) 중 큰 값을 선택
    dp[comp] = max(dp[i - 1] + val, dp[comp])

print(dp[-1])