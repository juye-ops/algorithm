from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(campus, y, x, N, M):
    ret = 0
    
    visited = [[False for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append((y, x))

    while q:
        i, j = q.popleft()

        ret += (campus[i][j] == 'P')

        for d in range(4):
            if (0 <= i+dy[d] < N and 0 <= j+dx[d] < M) and (campus[i+dy[d]][j+dx[d]] != 'X') and (not visited[i+dy[d]][j+dx[d]]):
                visited[i+dy[d]][j+dx[d]] = True
                q.append((i+dy[d], j+dx[d]))
    
    return ret


def solution(N, M, campus):
    x = y = None
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                y, x = i, j
                
    answer = bfs(campus, y, x, N, M)
    if answer == 0:
        answer = "TT"

    return answer


N, M = map(int, input().split())
campus = [input() for _ in range(N)]

print(solution(N, M, campus))