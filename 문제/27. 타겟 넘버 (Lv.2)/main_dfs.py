def dfs(acc, target, numbers, res) :
    if len(numbers) == 0:
        if acc == target :
            return res + 1
        else : 
            return res
        
    elem = numbers[0]
    res = dfs(acc+elem, target, numbers[1:], res)
    res = dfs(acc-elem, target, numbers[1:], res)
    
    return res

def solution(numbers, target):
    return dfs(0, target, numbers, 0)