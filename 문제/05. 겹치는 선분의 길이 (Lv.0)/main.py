from itertools import combinations

def solution(lines):
    
    overlap_set = set()
    
    for line1 , line2  in combinations(lines,2) :
        x1 = max(line1[0], line2[0])
        x2 = min(line1[1], line2[1])
        
        for i in range(x1,x2) :
            overlap_set.add(i)
        
    return len(overlap_set)