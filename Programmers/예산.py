def solution(d, budget):
    answer = 0
    price = 0
    d.sort()
    
    for i in d:
        if price + i > budget:
            return answer
        answer+=1
        price+=i
    return answer