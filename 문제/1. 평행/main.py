def calcGrad(point1, point2) :
    dy = point1[1]-point2[1]
    dx = point1[0]-point2[0]
    return dy/dx

def solution(dots):
    case1 = 1 if calcGrad(dots[0],dots[1]) == calcGrad(dots[2],dots[3]) else 0
    case2 = 1 if calcGrad(dots[0],dots[2]) == calcGrad(dots[1],dots[3]) else 0
    case3 = 1 if calcGrad(dots[0],dots[3]) == calcGrad(dots[1],dots[2]) else 0
    answer = case1 or case2 or case3
    
    return answer