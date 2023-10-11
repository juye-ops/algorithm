import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)] 
rpos = []
vpos = []
virus = 0
walls = 0
def init():
    global virus, walls
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                rpos.append((j, i))
            elif board[i][j] == 1:
                walls += 1
            elif board[i][j] == 2:
                virus += 1
                vpos.append((j, i))

def copy(board):
    return [x[:] for x in board]


def bfs(board, vpos, virus):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(M)] for x in range(N)]
    q = deque(vpos)

    while q:
        x, y = q.popleft()
        board[y][x] = 2

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not(0 <= nx < M and 0 <= ny < N):
                continue

            if board[ny][nx] == 0 and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = True
                virus += 1
    return virus

answer = 0
init()
for (ax, ay), (bx, by), (cx, cy) in combinations(rpos, 3):
    new_board = copy(board)
    new_board[ay][ax] = 1
    new_board[by][bx] = 1
    new_board[cy][cx] = 1
    
    v = bfs(new_board, vpos, virus)
    answer = max(N*M - (walls + 3 + v) , answer)
print(answer)