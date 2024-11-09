def validate(today, date, expires) :
    t_year, t_month, t_day = map(int,today.split('.'))
    year, month, day = map(int,date.split('.'))
    month = month + expires   
    day -= 1
    
    if month > 12 : 
        new_year = month // 12
        new_month = month % 12 
        
        year += new_year
        month = new_month
    
    if month == 0 :
        year -= 1
        month = 12

    if day < 1 :
        month -= 1
        day = 28
    
    
    if (t_year < year) :
        return True
    elif (t_year == year and t_month < month) :
        return True
    elif (t_year == year and t_month == month and t_day <= day) :
        return True
    
    return False
    

def solution(today, terms, privacies):
    mapping_table = {}
    expired = []

    for i in terms :
        key,val = i.split()
        mapping_table[key] = int(val)
    
    for idx, data in enumerate(privacies) :
        date, char = data.split()
        expires = mapping_table[char]
        if not (validate(today, date, expires)) :
            expired.append(idx + 1)
    
    return expired