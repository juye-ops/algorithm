def solution(n):
    if n in [0, 1]: return n
    a, b = 0, 1
    answer = 0
    for i in range(2, n+1):
        answer = a+b
        a, b = b, answer
    return answer%1234567