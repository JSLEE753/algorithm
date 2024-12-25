from itertools import permutations
def solution(expression):
    # 목표 : abs() 가 가장 큰 값 구하기
    arrs = list(map(lambda x : int(x) if x.isdecimal() else x , expression.replace('*',' * ').replace('+', ' + ').replace('-', ' - ').split()))
    result = 0
    for signs in permutations(['+','-','*'], 3) :
        copied = arrs[:]
        for sign in signs : 
            while(True) : 
                found = 0 # arrs에서 해당 기호가 존재?
                for i in range(len(copied)) : 
                    if copied[i] == sign : 
                        found += 1 
                        val1, val2 = copied[i-1], copied[i+1]
                        
                        if sign == '*' :
                            copied.insert(i-1, val1 * val2)
                                
                            
                        elif sign == '+' : 
                            copied.insert(i-1, val1 + val2)
                            
                        
                        else : 
                            copied.insert(i-1, val1 - val2)
                            
                        # 사용된 요소 삭제
                        for _ in range(3) : 
                            del copied[i]
                        
                        break
                
                if not found : # arrs에서 해당 기호가 없으면, 다음 sign을 검사
                    break
                    
        result = max(result, abs(copied[0]))
    
    return result

