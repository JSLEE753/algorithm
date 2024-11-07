def solution(board, moves):
    n = len(board)
    stack = [0]
    count = 0
    
    for move in moves :
        x_top = 0 
        y = move - 1
        for i in range(n) : 
            target = board[x_top][y]
            if target :
                board[x_top][y] = 0
                
                if stack[-1] == target :
                    count += 1
                    stack.pop()
                    break
                else : 
                    stack.append(target)                                
                    break
            else :
                x_top += 1
                
    return count * 2