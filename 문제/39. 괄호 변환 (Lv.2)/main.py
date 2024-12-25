# u,v 분리
def sep(w) : 
    cnt = 0
    for i in range(len(w)) : 
        if w[i] == '(' : 
            cnt += 1
        elif w[i] == ')' : 
            cnt -= 1
        
        if cnt == 0 : 
            return w[0:i+1], w[i+1:] if len(w)>2 else ''
    
# w가 유효한 문자열?
def isValid(w) : 
    cnt = 0
    for i in w : 
        if i == '(' :
            cnt += 1
        else : 
            cnt -= 1
        
        if cnt < 0 : 
            return False
        
    return True

# 유효한 문자열로 고치기
def fix(w) : 
    if w == '' : 
        return ''
    
    u,v = sep(w)
    
    if isValid(u) : 
        return u + fix(v)
    else :
        t = '('
        t += fix(v)
        t += ')'
        
        nu = ''
        for i in range(1,len(u)-1) : 
            if u[i] == '(' : 
                nu += ')'
            elif u[i] == ')' : 
                nu += '('
        t += nu
        
        return t
        
    
def solution(p):
    return fix(p)