def solution(a, b):
    a, b = min(a, b), max(a, b)
    return sum(range(a, b+1))