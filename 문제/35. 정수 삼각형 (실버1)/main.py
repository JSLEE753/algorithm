n = int(input())
arr = []
for _ in range(n) : 
  arr.append(list(map(int,input().split())))

for row_index in range(1,n) :
  for val_index in range(row_index+1) :
    # 맨 처음 수
    if val_index == 0 : 
      arr[row_index][val_index] += arr[row_index-1][val_index]
    # 맨 마지막 수
    elif val_index == row_index : 
      arr[row_index][val_index] += arr[row_index-1][val_index-1]
    # 그 외
    else : 
      arr[row_index][val_index] += max(arr[row_index-1][val_index-1] , arr[row_index-1][val_index])

print(max(arr[-1]))