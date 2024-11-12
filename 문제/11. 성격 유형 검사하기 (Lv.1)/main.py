def compare(result_dict, char1, char2) :
    if result_dict[char1] < result_dict[char2] :
        return char2
    else :
        return char1
    

def solution(survey, choices):
    result = ''
    result_dict = {'R' : 0 , 'T' : 0 , 'C' : 0 , 'F' : 0, 'J' : 0 , 'M' : 0 , 'A' : 0 , 'N' : 0}
    
    choices = list(map(lambda x : x - 4 , choices))

    for idx, choice in enumerate(choices) : 
        if choice < 0 :
            result_dict[survey[idx][0]] += abs(choices[idx])
        else :
            result_dict[survey[idx][1]] += abs(choices[idx])
    
    
    result += compare(result_dict,'R','T')
    result += compare(result_dict,'C','F')
    result += compare(result_dict,'J','M')
    result += compare(result_dict,'A','N')
        
    return result