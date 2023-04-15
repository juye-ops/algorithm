def solution(routes):
    answer = 0
    routes.sort()
    now = -30000
    for i in routes:
        if i[0] <= now:
            now = min(now, i[1])
        else:
            answer+=1
            now = i[1]
        
    return answer