from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(v, graph):
    visited = [[False for x in range(M)] for y in range(N)]
    q = deque()
    q.append(v)
    answers = []
    while q:
        x, y = q.popleft()
        if x == M-1 and y == N-1:
            return graph[y][x]
        visited[y][x] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0 <= nx < M and 0 <= ny < N): continue
            if not (not visited[ny][nx]): continue
            if (graph[ny][nx] == 1):
                graph[ny][nx] = int(graph[y][x]) + 1
                q.append((nx, ny))


def solution(W, H):
    global N, M, visited
    N, M = W, H
    MAP = [list(map(int, list(input()))) for x in range(N)]
    print(bfs((0, 0), MAP))



solution(*map(int, input().split()))