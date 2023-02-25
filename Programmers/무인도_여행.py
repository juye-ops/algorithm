from collections import deque
def bfs(maps, visited, N, M, x, y):
    ret = 0
    q = deque()
    now = (x, y, int(maps[y][x]))
    q.append(now)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        x, y, now = q.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True
        ret += now
        for i in range(4):
            if 0 <= x + dx[i] < M and 0 <= y + dy[i] < N:
                if maps[y + dy[i]][x + dx[i]] != "X" and not visited[y + dy[i]][x + dx[i]]:
                    q.append((x+dx[i], y+dy[i], int(maps[y+dy[i]][x+dx[i]])))
                    
    return ret
        
        

def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    answer = []
    for y in range(N):
        for x in range(M):
            if maps[y][x] != "X" and not visited[y][x]:
                answer.append(bfs(maps, visited, N, M, x, y))
        
    return sorted(answer) if answer else [-1]