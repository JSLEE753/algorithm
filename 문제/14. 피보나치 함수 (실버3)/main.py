n = int(input())
input_arr = []
max_val = 0
for i in range(n) :
  new_input = (int(input()))
  input_arr.append(new_input)
  max_val = max(new_input,max_val)

arr = [[0,0]] * (max_val + 2)
arr[0], arr[1] = [1,0] , [0,1]

for i in range(2, max_val + 2) :
  val = [x + y for x,y in zip(arr[i-1],arr[i-2])]
  arr[i] = val
  print(val)


for i in input_arr :
  print(arr[i][0],arr[i][1])
