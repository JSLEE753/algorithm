def solution(babbling):
    speakables = ['aya', 'ye', 'woo', 'ma']
    count = 0
    
    for word in babbling :
        for speakable in speakables :
            if speakable in word :
                word = word.replace(speakable,' ')
        if (word.strip() == '') :
            count += 1
            
    return count