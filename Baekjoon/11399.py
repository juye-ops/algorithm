def solution(N, P):
    answer = 0
    T = 0
    P.sort()
    for i in P:
        T += i
        answer += T
    return answer
    
N = int(input())
P = list(map(int, input().split()))

print(solution(N, P))