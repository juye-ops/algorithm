from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 정상인
def bfs_a(N, RGB, visited, i, j, color):
    q = deque()
    now = (i, j)
    q.append(now)

    while q:
        i, j = q.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = True

        for d in range(4):
            if 0 <= i + dy[d] < N and 0 <= j + dx[d] < N and RGB[i+dy[d]][j+dx[d]] == color:
                q.append((i+dy[d], j+dx[d]))

# 적록색약
def bfs_b(N, RGB, visited, i, j, color):
    q = deque()
    now = (i, j)
    q.append(now)

    blue = (color == 'B')

    while q:
        i, j = q.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = True

        for d in range(4):
            if 0 <= i + dy[d] < N and 0 <= j + dx[d] < N:
                if (blue and RGB[i+dy[d]][j+dx[d]] == 'B') or (not blue and RGB[i+dy[d]][j+dx[d]] != 'B'):
                    q.append((i+dy[d], j+dx[d]))

def solution(N, RGB):
    visited_a = [[False for _ in range(N)] for _ in range(N)]
    visited_b = [[False for _ in range(N)] for _ in range(N)]
    a = b = 0
    for i in range(N):
        for j in range(N):
            color = RGB[i][j]
            if visited_a[i][j] == False:
                bfs_a(N, RGB, visited_a, i, j, color)
                a+=1
            if visited_b[i][j] == False:
                bfs_b(N, RGB, visited_b, i, j, color)
                b+=1
    
    print(a, b)


N = int(input())
RGB = [input() for _ in range(N)]

solution(N, RGB)