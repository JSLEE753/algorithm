def solution(n):
    directions = [(0,1) , (1,0) , (0,-1), (-1,0)]
    arr = [[1] * n for row in range(n)]
    if (n % 2 == 1) :
        arr[n//2][n//2] = n**2
    x, y = 0, 0
    count = 1
    
    while(True) :
        for i, direction in enumerate(directions) :
            for j in range(n-1) :

                arr[x][y] = count 
                count += 1

                if (i == 3 and j == n-2):
                    y = y + 1
                else : 
                    x = x + direction[0]
                    y = y + direction[1]
                
        n -= 2
        
        
        if (n<2) :
            break
            
        
    return arr    