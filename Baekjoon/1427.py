def solution(n):
    return "".join(sorted(n, reverse=True))


print(solution(input()))
