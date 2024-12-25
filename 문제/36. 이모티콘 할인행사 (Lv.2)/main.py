import itertools
def solution(users, emoticons):
    sales = (60, 70, 80, 90)
    n = len(emoticons)
    res = []
    max_join = 0
    
    for idx in range(len(users)) : 
        if (users[idx][0] % 10 != 0) : 
            users[idx][0] += 10 - users[idx][0] % 10 
    
    for sales_p in itertools.product(sales,repeat = n) : 
        tmp_emoticons = [ (sales_p[i]) / 100 * (emoticons[i]) for i in range(n)]
        
        join_cnt = 0
        sold_cnt = 0
        
        for idx, user in enumerate(users) : 
            buy = 0
            for i in range(n): 
                if (100 - (sales_p[i])) >= (user[0]) :
                    buy += tmp_emoticons[i]
                    
            if buy >= user[1] :
                join_cnt += 1
                buy = 0
            sold_cnt += buy
        
        max_join = max(join_cnt,max_join)
        res.append((join_cnt,sold_cnt))
        
    res_val = 0        
    for i in res : 
        if i[0] == max_join :
            res_val = max(res_val, i[1])
    
    result = [max_join,res_val]
    return result