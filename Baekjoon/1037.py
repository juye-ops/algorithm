def solution(n):
    divisors = list(map(int, input().split()))
    return min(divisors) * max(divisors)

print(solution(int(input())))