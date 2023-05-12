def solution(targets):
    answer = 1
    targets.sort(key = lambda x: x[1])
    b = targets[0][1]
    for i, j in targets:
        if i >= b:
            b = j
            answer += 1
    return answer