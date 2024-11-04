def solution(s):
    arr = ['zero', 'one', 'two', 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' ,'nine']
    
    while(not s.isnumeric()):
        for index, string in enumerate(arr) :
            if(string in s) :
                s = s.replace(arr[index], str(index))
    
    return int(s)