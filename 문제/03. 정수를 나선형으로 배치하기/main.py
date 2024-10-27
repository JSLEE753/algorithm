def solution(n):
    arr = [[1 for col in range(n)] for row in range(n)]
    iter_num = n - 1
    rot = 0
    count = 0
    directions = ['right' , 'down' , 'left' , 'up']
    
    while(iter_num >= 1) :
        for direction in directions : 
            for i in range(rot, iter_num) :
                count += 1
                if (direction == 'right') :
                    arr[rot][i] = count
                if (direction == 'down') :
                    arr[i][n-1-rot] = count
                if (direction == 'left') :
                    arr[n-1-rot][n-1-i] = count
                if (direction == 'up') :
                    arr[n-1-i][rot] = count
            
            
        if (rot == iter_num) :
            count += 1
            arr[rot][rot] = count
        
        if (count == n * n) :
            break

        iter_num -= 1
        rot += 1
            
    return arr