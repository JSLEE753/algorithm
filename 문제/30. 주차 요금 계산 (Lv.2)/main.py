from collections import defaultdict
import math

def get_minutes(arr) : 
    acc = 0
    last_minutes = 0
    for idx, time in enumerate(arr) :
        h, m = time.split(':')
        nm = int(h) * 60 + int(m)
        # in
        if idx % 2 == 0 :
            last_minutes = nm
        # out
        else : 
            acc += nm - last_minutes
    return acc

def get_fees(minute, fees) : 
    if minute <= fees[0] :
        return fees[1]
    else : 
        return fees[1] + math.ceil(((minute - fees[0]) / fees[2])) * fees[3]

def solution(fees, records):
    table = defaultdict(list)
    result = defaultdict(int)
    # table : {num : [check, [intime,outtime]]}
    for record in records : 
        time, num, inout = record.split()
        table[num].append(time)
    
    for key in table.keys() : 
        if len(table[key]) % 2 == 1 : 
            table[key].append('23:59')
        
        result[key] = get_fees(get_minutes(table[key]), fees)
        
    result = dict(result)
    sorted_arr = sorted(result.items())
    answer = [x[1] for x in sorted_arr]
            
            
    return answer