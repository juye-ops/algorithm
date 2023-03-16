def solution(N):
    val = 1
    for i in range(1, N+1):
        val *= i
    
    answer = 0
    for i in reversed(str(val)):
        if i == '0':
            answer += 1
        else: break
    return answer


def _solution(N):
    answer = 0
    for i in range(1, N+1):
        if i%5 == 0:
            answer += 1
        if i%25 == 0:
            answer += 1
        if i%125 == 0:
            answer += 1
    return answer

N = int(input())
print(solution(N))