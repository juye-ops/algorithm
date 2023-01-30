def solution(want, number, discount):
    answer = 0
    target = dict(zip(want, number))
    count = {}
    for idx, x in enumerate(discount):
        if count.get(x) is None:
            count[x] = 0
        count[x]+=1
        
        if idx >= 10:
            count[discount[idx-10]]-=1
            if count[discount[idx-10]] == 0:
                del count[discount[idx-10]]
        
        answer+=(target==count)
    
    return answer