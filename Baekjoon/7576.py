from collections import deque

def bfs(tomato, q):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        y, x = q.popleft()
        day = tomato[y][x]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if tomato[ny][nx] == 0:
                    tomato[ny][nx] = day+1
                    q.append((ny, nx))

def solution(M, N, tomato):
    answer = 0
    q = deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:   # 1인 부분부터 다 집어넣은 채로 각각의 region에서 bfs를 멀티프로세스처럼 진행
                q.append((i, j))
    bfs(tomato, q)
    
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                return -1
            answer = max(answer, tomato[i][j])
    return answer - 1

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
print(solution(M, N, tomato))