from collections import deque 

result = 0

def bfs(numbers,target) :
    global result
        
    # [number, level, acc]
    queue = deque([[numbers[0],0,0] , [-numbers[0],0,0]])
    
    while(queue) :
        elem, level, acc = queue.popleft()
        level += 1
        acc += elem
        
        if level == len(numbers)  :
            if acc == target : 
                result += 1
                continue
            else : 
                continue
        
        if level < len(numbers)   : 
            queue.append([numbers[level], level, acc])
            queue.append([-numbers[level], level, acc])
    
def solution(numbers, target):
    bfs(numbers,target)
    return result