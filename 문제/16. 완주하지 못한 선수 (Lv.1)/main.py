from collections import Counter

def solution(participant, completion):
    counter_p = Counter(participant)
    counter_c = Counter(completion)
    answer = ''
    for name in counter_p :
        if (counter_p[name] != counter_c[name]) :
            answer = name
            break
    
    return answer