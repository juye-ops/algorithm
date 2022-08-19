from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(MAP, visited, x, y, n):
    q = deque()
    q.append((x, y))
    cnt = 0
    while q:
        nx, ny = q.popleft()
        if visited[ny][nx]: continue
        visited[ny][nx] = True
        cnt+=1
        for i in range(4):
            if 0<=ny+dy[i]<n and 0<=nx+dx[i]<n and  MAP[ny+dy[i]][nx+dx[i]] == "1":
                q.append((nx+dx[i], ny+dy[i]))
    return cnt




def solution(n):
    MAP = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    answers = []
    for _ in range(n):
        MAP.append(input())


    for i in range(n):
        for j in range(n):
            if MAP[i][j] == "1" and not visited[i][j]:
                answers.append(bfs(MAP, visited, j, i, n))

    print(len(answers))
    for i in sorted(answers):
        print(i)


solution(int(input()))