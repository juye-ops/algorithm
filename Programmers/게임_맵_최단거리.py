from collections import deque


def solution(maps):
    answer = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for x in range(n)]

    q = deque()
    q.append((0, 0, 1))
    while q:
        x, y, cnt = q.popleft()
        if x == m-1 and y == n-1:
            return cnt
        if not (0<=x<m and 0<=y<n):
            continue
        if visited[y][x] or not maps[y][x]:
            continue

        visited[y][x] = True
        for i in range(4):
            q.append((x+dx[i], y+dy[i], cnt+1))
    return -1