def solution(N, M, S):
    answer = 0

    p1 = p2 = 0
    while p2 < M:
        if S[p2:p2+3] == 'IOI':
            p2 += 2
            if p2 - p1 >= 2 * N:
                p1 += 2
                answer += 1
        else:
            p1 = p2 + 1
            p2 = p2 + 1
    
    return answer
        

N = int(input())
M = int(input())
S = input()

print(solution(N, M, S))