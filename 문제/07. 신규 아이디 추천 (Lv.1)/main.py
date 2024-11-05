def solution(new_id):
    # a = 97 , z = 122
    # 0 = 48 , 9 = 57
    # - = 45 , . = 46 , _ = 95
    
    # 1단계 - 소문자 치환
    new_id = new_id.lower()
    print(f'1단계 : new_id = {new_id}')
    
    # 2단계 - 이외의 문자 제거
    for char in new_id :
        if not ((97 <= ord(char) <= 122) or (48 <= ord(char) <= 57) or char == '-' or char == '.' or char == '_') :
            new_id = new_id.replace(char,'')
            
    print(f'2단계 : new_id = {new_id}')
    
            
    # 3단계 - 마침표 2번 연속인 부분을 하나의 마침표로
    
    while(True) :
        if ('..' in new_id) :
            new_id = new_id.replace('..','.')
        else : 
            break
            
    print(f'3단계 : new_id = {new_id}')
            
    # 4단계 = 마침표가 처음이나 끝에 위치하면 제거

    while(True) :
        if new_id == '.' :
            new_id = ''
            break
        
        if new_id[0] == '.' and new_id[-1] == '.' :
            new_id = new_id.strip('.')
        elif new_id[0] =='.' :
            new_id = new_id.lstrip('.')
        elif new_id[-1] == '.' :
            new_id = new_id.rstrip('.')
        else : 
            break
            
    print(f'4단계 : new_id = {new_id}')
    
    # 5단계 - 빈 문자열일 경우, a 대입
    if (new_id == '') :
        new_id = 'a'
        
    print(f'5단계 : new_id = {new_id}')
    
    # 6단계 - 16자 이상이면 15개 문자까지만 표시, 마침표가 끝에 위치한 경우 제거
    
    if (len(new_id) >= 16) : 
        new_id = new_id[:15]
    
    while(True) :
        if(new_id[-1] == '.') :
            new_id = new_id[:-1]
        else :
            break
            
    print(f'6단계 : new_id = {new_id}')
    
    
    # 7단계 - 2자 이하면, 마지막 문자를 길이가 3이될때까지 반복 
    
    while (len(new_id) <= 2) : 
        new_id += new_id[-1]
        
    print(f'7단계 : new_id = {new_id}')
    
    return new_id


