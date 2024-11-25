from collections import defaultdict

def solution(bandage, health, attacks):
    max_health = health
    time_limit = attacks[-1][0]
    casting_time = bandage[0]
    heal = bandage[1]
    bonus_heal = bandage[2]
    attacks_table = defaultdict(int)
    for attack in attacks :
        attacks_table[attack[0]] = attack[1] 
        
    successive_t = 0
    
    for time in range(time_limit+1) : 
        if(attacks_table[time]) : 
            successive_t = 0
            health = health - attacks_table[time]
        else : 
            health = min(max_health, health + heal)
            successive_t += 1
        
        if successive_t == casting_time : 
            health = min(max_health, health + bonus_heal)
            successive_t = 0
        
        if health <= 0 :
            return -1
        
    return health

