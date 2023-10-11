N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

side = [0, 0, 0, 0] # 정면, 왼, 뒤, 오른
up = 0
down = 0

def roll_right():
    global up, down
    up, side[1], down, side[3] = side[1], down, side[3], up

def roll_left():
    global up, down
    up, side[1], down, side[3] = side[3], up, side[1], down

def roll_up():
    global up, down
    up, side[0], down, side[2] = side[0], down, side[2], up

def roll_down():
    global up, down
    up, side[0], down, side[2] = side[2], up, side[0], down


def copy_num():
    global up, down
    if board[y][x] == 0:
        board[y][x] = down
    elif board[y][x]:
        down = board[y][x]
        board[y][x] = 0


funcs = {
    1: roll_right,
    2: roll_left,
    3: roll_up,
    4: roll_down
}

for d in commands:
    if not(0 <= x+dx[d-1] < M and 0 <= y+dy[d-1] < N):
        continue
    x, y = x+dx[d-1], y+dy[d-1]
    funcs[d]()
    copy_num()
    print(up)