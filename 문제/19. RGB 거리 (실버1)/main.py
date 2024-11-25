n = int(input())
inputs = []
for i in range(n) :
  inputs.append(list(map(int,input().split())))

for i in range(1,n) :
  inputs[i][0] = inputs[i][0] + min(inputs[i-1][1],inputs[i-1][2])
  inputs[i][1] = inputs[i][1] + min(inputs[i-1][0],inputs[i-1][2])
  inputs[i][2] = inputs[i][2] + min(inputs[i-1][0],inputs[i-1][1])

print(min(inputs[-1]))
