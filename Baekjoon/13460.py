import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

board = [input()[:-1] for _ in range(N)]

rx, ry = (-1, -1)
bx, by = (-1, -1)

for y in range(N):
    for x in range(M):
        if board[y][x] == "R":
            rx, ry = x, y
        if board[y][x] == "B":
            bx, by = x, y

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = set()
visited.add((rx, ry, bx, by))

def bfs(marble_r: tuple, marble_b: tuple):
    '''
    marble_r: 최초 r 좌표(rx, ry)
    marble_b: 최초 b 좌표(bx, by)
    '''
    q = deque()
    q.append((marble_r, marble_b, 0)) # r좌표, b좌표, 카운트

    while q:
        (rx, ry), (bx, by), cnt = q.popleft()
        if cnt >= 10:
            continue

        for d in range(4):
            # red move
            R_state = False
            B_state = False
            nrx, nry = rx, ry
            nbx, nby = bx, by

            while True:
                if board[nry+dy[d]][nrx+dx[d]] == "#": # toward wall
                    break
                elif board[nry+dy[d]][nrx+dx[d]] == "O": # meet end
                    nrx+=dx[d]
                    nry+=dy[d]
                    R_state = True
                    break
                else: 
                    nrx+=dx[d]
                    nry+=dy[d]
                    
            while True:
                if board[nby+dy[d]][nbx+dx[d]] == "#": # toward wall
                    break
                elif board[nby+dy[d]][nbx+dx[d]] == "O":
                    nbx+=dx[d]
                    nby+=dy[d]
                    B_state = True
                    break
                else:
                    nbx+=dx[d]
                    nby+=dy[d]

            if R_state and not B_state:
                return cnt+1
            elif not R_state and B_state:
                continue
            elif R_state and B_state:
                continue

            if nrx == nbx and nry == nby: # if B and R in same position
                if (abs(nrx - rx) + abs(nry - ry)) < (abs(nbx - bx) + abs(nby - by)):
                    nbx-=dx[d]
                    nby-=dy[d]
                elif (abs(nrx - rx) + abs(nry - ry)) > (abs(nbx - bx) + abs(nby - by)):
                    nrx-=dx[d]
                    nry-=dy[d]
            
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append(((nrx, nry), (nbx, nby), cnt+1))

    return -1

print(bfs((rx, ry), (bx, by)))
