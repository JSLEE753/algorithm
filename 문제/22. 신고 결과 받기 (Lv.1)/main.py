from collections import defaultdict
def solution(id_list, report, k):
    
    report = list(set(report))
    res = defaultdict(int)
    a = defaultdict(int)
    
    for i in report : 
        reporter, reported = i.split()
        res[reported] += 1
    for i in report : 
        reporter, reported = i.split()
        if res[reported] >= k :
            a[reporter] += 1
    
    result = []
    for id in id_list : 
        result.append(a[id])
    
        
    return result