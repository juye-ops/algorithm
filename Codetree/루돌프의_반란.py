import sys
input = sys.stdin.readline

N, M, P, C, D = map(int, input().split())
ry, rx = map(int, input().split())
rx-=1
ry-=1

board = [[0 for _ in range(N)] for _ in range(N)]
board[ry][rx] = -1

santa = {p: [] for p in range(1, P+1)}
for _ in range(P):
    i, y, x = map(int, input().split())
    santa[i] = [(x-1, y-1), 0, False, 0] # (x, y), score, failure, stun
    board[y-1][x-1] = i

def l2_distance(x1, y1, x2, y2):
    return (y2-y1)**2 + (x2-x1)**2

def r_choose_s():
    ret = None
    distance = float("INF")
    
    for i in santa:
        (sx1, sy1), score, failure, stun = santa[i]
        if failure:
            continue

        dist = l2_distance(sx1, sy1, rx, ry)
        if dist < distance:
            ret = i
            distance = dist
        elif dist == distance:
            (sx2, sy2), _, _, _ = santa[ret]
            if sy1 > sy2:
                ret = i
            elif sy1 == sy2:
                if sx1 > sx2:
                    ret = i
    return ret

# d는 12시에서 시계방향
# 북동남서 순으로 0, 2, 4, 6
dx = [0, 1, 1, 1, 0, -1, -1, -1] 
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def interaction(s, nsx, nsy, d):
    while board[nsy][nsx]:
        santa[s][0] = (nsx, nsy)
        s, board[nsy][nsx] = board[nsy][nsx], s
        nsx += dx[d]
        nsy += dy[d]
        if not (0 <= nsx < N and 0 <= nsy < N):
            santa[s][2] = True
            santa[s][0] = (-1, -1)
            break
    else:
        santa[s][0] = (nsx, nsy)
        board[nsy][nsx] = s

def move_r():
    global rx, ry
    s = r_choose_s()
    (sx, sy), _, _, _ = santa[s]
    direction = None
    distance = float("INF")
    for d in range(8):
        dist = l2_distance(rx+dx[d], ry+dy[d], sx, sy)
        if dist < distance:
            direction = d
            distance = dist



    board[ry][rx] = 0
    rx+=dx[direction]
    ry+=dy[direction]
    
    # 충돌
    if board[ry][rx]:
        santa[s][1] += C
        santa[s][3] = 2
        nsx = sx+C*dx[direction]
        nsy = sy+C*dy[direction]
        if not (0 <= nsx < N and 0 <= nsy < N):
            santa[s][2] = True
            santa[s][0] = (-1, -1)
        elif board[nsy][nsx]:
            interaction(s, nsx, nsy, direction)
        else:
            board[nsy][nsx] = s
            santa[s][0] = (nsx, nsy)


    board[ry][rx] = -1

def move_s():
    for s in santa:
        (sx, sy), score, failure, stun = santa[s]
        if failure or stun:
            continue

        direction = None
        distance = l2_distance(sx, sy, rx, ry)
        for d in range(0, 8, 2):
            dist = l2_distance(sx+dx[d], sy+dy[d], rx, ry)
            if not (0 <= sx+dx[d] < N and 0 <= sy+dy[d] < N):
                continue
            if dist < distance and board[sy+dy[d]][sx+dx[d]] <= 0:
                distance = dist
                direction = d
        
        if direction is None:
            continue
        
        board[sy][sx] = 0
        sx+=dx[direction]
        sy+=dy[direction]
        
        # 충돌
        if board[sy][sx] == -1:
            direction = (direction+4) % 8
            santa[s][1] += D
            santa[s][3] = 2
            nsx = sx+D*dx[direction]
            nsy = sy+D*dy[direction]
            if not (0 <= nsx < N and 0 <= nsy < N):
                santa[s][2] = True
                santa[s][0] = (-1, -1)
            elif board[nsy][nsx]:
                interaction(s, nsx, nsy, direction)
            else:
                santa[s][0] = (nsx, nsy)
                board[nsy][nsx] = s
        else:
            santa[s][0] = (sx, sy)
            board[sy][sx] = s
        
        

for m in range(M):

    move_r()
    move_s()
    failure = True
    for i in santa:
        if not santa[i][2]:
            failure = False
            santa[i][1]+=1
        if santa[i][3]:
            santa[i][3] -= 1
    if failure:
        break

for i in santa:
    print(santa[i][1], end=" ")