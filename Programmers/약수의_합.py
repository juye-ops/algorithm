def solution(n):
    return sum([x if n%x == 0 else 0 for x in range(1,n+1)])