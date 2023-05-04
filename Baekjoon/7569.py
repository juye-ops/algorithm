import sys
from collections import deque

input = sys.stdin.readline

def bfs(tomato, q, H, N, M):
    dh = [-1, 1, 0, 0, 0, 0]
    dn = [0, 0, -1, 1, 0, 0]
    dm = [0, 0, 0, 0, -1, 1]

    while q:
        h, n, m = q.popleft()

        for i in range(6):
            if (0 <= h+dh[i] < H) and (0 <= n+dn[i] < N) and (0 <= m+dm[i] < M):
                if tomato[h+dh[i]][n+dn[i]][m+dm[i]] == 0:
                    q.append((h+dh[i], n+dn[i], m+dm[i]))
                    tomato[h+dh[i]][n+dn[i]][m+dm[i]] = tomato[h][n][m] + 1


def solution(M, N, H, tomato):
    q = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 1:
                    q.append((h, n, m))
    bfs(tomato, q, H, N, M)
    answer = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 0:
                    return -1
                answer = max(answer, tomato[h][n][m])
    
    return answer - 1

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print((solution(M, N, H, tomato)))