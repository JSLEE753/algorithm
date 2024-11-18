n = int(input())
targets = []
for i in range(n) : 
  targets.append(int(input()))

def f(target,acc) : 
  count = 0
  if acc == target :
    count += 1
  
  if (acc + 1 <= target) :
    count += f(target,acc + 1)

  if (acc + 2 <= target) :
    count += f(target,acc + 2)

  if (acc + 3 <= target) :
    count += f(target,acc + 3)

  return count 

for target in targets :
  print(f(target,0))


