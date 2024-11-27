from collections import defaultdict

def solution(friends, gifts):
    friend_dict = defaultdict(list)
    result_dict = defaultdict(int)
    for friend in friends : 
        personal_dict = defaultdict(int)
        # [선물지수, 이름 : 준 횟수]
        friend_dict[friend] = [0,personal_dict]

    for gift in gifts : 
        sender, receiver = gift.split()
        friend_dict[sender][1][receiver] += 1
        friend_dict[sender][0] += 1
        friend_dict[receiver][0] -= 1

    
    for sender in friend_dict : 
        for receiver in friends :
            if sender == receiver :
                continue
            elif friend_dict[sender][1][receiver] > friend_dict[receiver][1][sender] :
                result_dict[sender] += 1
                print(f'{sender}는 선물을 더 많이 줬던 {receiver}에게서 선물을 하나 받음.')
            elif friend_dict[sender][1][receiver] == friend_dict[receiver][1][sender] :
                if friend_dict[sender][0] > friend_dict[receiver][0] : 
                    result_dict[sender] +=1
                    print(f'{sender}는 선물을 주고받지 않았던 {receiver}보다 커 선물을 하나 받음')
    
    result = list(result_dict.values())
    
    if len(result) == 0 :
        return 0
    else :
        return max(result)