import sys
input = sys.stdin.readline

def solution(N, K, Bills):
    answer = 0
    for b in Bills[::-1]:
        q, r = divmod(K, b)
        K = r
        answer += q
    
    return answer

N, K = map(int, input().split())
Bills = [int(input()) for _ in range(N)]

print(solution(N, K, Bills))