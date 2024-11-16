
n = int(input())

result = 2000
result_arr = []
for i in range(2000) : 
    k = n 
    k -= 5 * i
    if ( k % 3 == 0 and k >= 0) :
        result = min(result, i + k // 3)

if result == 2000 :
    result = -1
print(result)