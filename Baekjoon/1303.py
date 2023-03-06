from collections import deque

def bfs(field, visited, now, team):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    ret = 0
    q = deque()
    q.append(now)
    while q:
        y, x = q.popleft()
        if visited[y][x]:
            continue
        
        visited[y][x] = True
        ret += 1
        
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if not visited[y + dy[i]][x + dx[i]] and field[y + dy[i]][x + dx[i]] == team:
                    q.append((y + dy[i], x + dx[i]))
    
    return ret
        
    

def solution(N, M, field):
    answer = {"W": 0, "B": 0}
    
    visited = [[False for _ in range(N)] for _ in range(M)]
    w = b = 0
    
    for y in range(M):
        for x in range(N):
            if not visited[y][x]:
                now = (y, x)
                team = field[y][x]
                answer[team] += bfs(field, visited, now, team)**2
    
    
    return f"{answer['W']} {answer['B']}"

N, M = map(int, input().split())
field = [input() for _ in range(M)]

print(solution(N, M, field))