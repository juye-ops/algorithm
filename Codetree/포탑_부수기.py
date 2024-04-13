from collections import deque
from copy import deepcopy

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
before = [[0 for _ in range(M)] for _ in range(N)]

def select_attacker():
    ap = float('INF')
    x = y = -1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                continue
            
            if ap == board[i][j]:
                if before[y][x] > before[i][j]:
                    continue
                elif before[y][x] == before[i][j]:
                    if x+y > i+j:
                        continue
                    elif x+y == i+j:
                        if x > j:
                            continue

            elif ap < board[i][j]:
                continue

            ap = board[i][j]
            x, y = (j, i)

    return x, y

def select_target():
    ap = -1
    x = y = -1
    for i in range(N):
        for j in range(M):
            if j == ax and i == ay:
                continue

            if board[i][j] == 0:
                continue
            
            if ap == board[i][j]:
                if before[y][x] < before[i][j]:
                    continue
                elif before[y][x] == before[i][j]:
                    if x+y < i+j:
                        continue
                    elif x+y == i+j:
                        if x < j:
                            continue

            elif ap > board[i][j]:
                continue

            ap = board[i][j]
            x, y = (j, i)
    
    return x, y


dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]

def attack_laser(ax, ay, tx, ty): # bfs
    q = deque()
    q.append((ax, ay, [(ax, ay)]))
    visited = [[False for _ in range(M)] for _ in range(N)]
    while q:
        x, y, route  = q.popleft()
        for d in range(0, 8, 2):
            nx = (x+dx[d]) % M
            ny = (y+dy[d]) % N
            if visited[ny][nx]: continue
            if board[ny][nx] == 0: continue

            if nx == tx and ny == ty:
                route.append((nx, ny))
                return route

            tmp_route = route[:]
            tmp_route.append((nx, ny))
            visited[ny][nx] = True
            q.append((nx, ny, tmp_route))
    
    else:
        return []
    
def attack_bomb(ax, ay, tx, ty):
    ret = [(ax, ay), (tx, ty)]
    for d in range(8):
        ret.append(((tx+dx[d])%M, (ty+dy[d])%N))
    return ret




for k in range(K):
    attacked = [[True for _ in range(M)] for _ in range(N)]
    ax, ay = select_attacker()
    before[ay][ax] = k+1
    tx, ty = select_target()
    if (tx == -1 and ty == -1):
        break
    ap = board[ay][ax] + N+M
    board[ay][ax] = ap
    
    # attack
    history = attack_laser(ax, ay, tx, ty) # attack1
    if not history:
        history = attack_bomb(ax, ay, tx, ty) # attack2

    for hx, hy in history:
        attacked[hy][hx] = False
        if hx == ax and hy == ay:
            continue
        elif hx == tx and hy == ty:
            board[hy][hx] = max(0, board[hy][hx]-ap)
        else:
            if board[hy][hx]:
                board[hy][hx] = max(0, board[hy][hx]-(ap//2))

    # maintain
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                board[i][j] += attacked[i][j]

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, board[i][j])

print(answer)