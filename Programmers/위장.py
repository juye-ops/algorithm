def solution(clothes):
    items = {}
    answer = 1
    for i in clothes:
        if items.get(i[1]) is None:
            items[i[1]] = 1 # 안입은 경우도 리스트에 포함해서 최종적으로 모두 안입은 1을 빼줌
        items[i[1]]+=1
    
    for i in items.values():
        answer *= i
    
    return answer-1