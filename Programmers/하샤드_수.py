def solution(x):
    answer = not (x % sum(list(map(int, list(str(x))))))
    return answer