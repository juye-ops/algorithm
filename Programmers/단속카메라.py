def solution(routes):
    answer = 1
    routes.sort(key = lambda x: x[1])
    now = routes[0][1]
    for i in routes:
        if now < i[0]:
            answer += 1
            now = i[1]
    return answer
