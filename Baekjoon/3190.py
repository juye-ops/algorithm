from collections import deque

N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
directions = {}
for i in range(L):
    s, d = input().split()
    directions[int(s)] =  d

board = [[0 for _ in range(N)] for _ in range(N)] # 0=길 -1=뱀, 1=사과

for ay, ax in apples:
    board[ay-1][ax-1] = 1

dx = [1, 0, -1, 0]  #+1 = 오른쪽, -1= 왼쪽
dy = [0, 1, 0, -1]

board[0][0] = -1
spos = deque([(0, 0)])
d = 0

def move_snake():
    def cut_tail():
        tx, ty = spos.popleft()
        board[ty][tx] = 0

    hx, hy = spos[-1] # head_x, head_y
    nhx, nhy = hx + dx[d], hy + dy[d]   # next_head_x, next_head_y
    
    if not (0<=nhx<N and 0<=nhy<N) or board[nhy][nhx] == -1:
        return False
    
    if board[nhy][nhx] != 1: # 길 이라면 꼬리 자르기
        cut_tail()

    board[nhy][nhx] = -1
    spos.append((nhx, nhy))
    return True


cnt = 0
while True:
    if not move_snake():
        break
    cnt += 1
    if directions.get(cnt) is not None:
        nd = directions[cnt]
        if nd == "L":
            d = (d-1)%4
        elif nd == "D":
            d = (d+1)%4

print(cnt+1)