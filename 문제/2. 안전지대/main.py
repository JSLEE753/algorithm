def solution(board):
        
    safeArr = [[0 for col in range(len(board[0]))] for row in range(len(board))] 
    n = len(board)
    count = 0
    
    for i in range(n) :
        for j in range(n) :
            if (board[i][j] == 1) :
                unsafeX = [i + dx for dx in [-1,0,1] if 0<= i + dx < n]
                unsafeY = [j + dy for dy in [-1,0,1] if 0<= j + dy < n]
                
                for x in unsafeX :
                    for y in unsafeY :
                        safeArr[x][y] = 1
                
    for row in safeArr : 
        count += row.count(0)
    
    return count