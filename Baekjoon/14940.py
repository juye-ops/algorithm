import sys
input = sys.stdin.readline

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(board, n, m, y, x, answer):
    q = deque()
    q.append((y, x, 0))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[y][x] = True
    while q:
        y, x, val = q.popleft()

        if board[y][x] == 0:
            answer[y][x] = 0
            continue
        else:
            answer[y][x] = max(answer[y][x], val)

        for i in range(4):
            if 0 <= y + dy[i] < n and 0 <= x + dx[i] < m:
                if not visited[y + dy[i]][x + dx[i]]:
                    q.append((y + dy[i], x + dx[i], board[y + dy[i]][x+dx[i]] * val+1))
                    visited[y + dy[i]][x + dx[i]] = True

    return answer


def solution(n, m, board):
    answer = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                y, x = i, j
            
            elif board[i][j] == 0:
                answer[i][j] = 0
    
    
    return map(lambda x: ' '.join(map(str, x)), bfs(board, n, m, y, x, answer))




n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(*solution(n, m, board), sep="\n")