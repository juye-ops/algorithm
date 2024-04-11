import sys
input = sys.stdin.readline

N, M = map(int, input().split())

y, x, d = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(N)]


def check_news():
    for i in range(4):
        if board[y+dy[i]][x+dx[i]] == 0:
            return True
    return False

answer = 0
while True:
    # action 1
    if not board[y][x]:
        board[y][x] = 2
        answer += 1
    
    # action 2
    while board[y][x] != 1:
        if not check_news():
            x-=dx[d]
            y-=dy[d]
        else: break
    else:
        break

    
    # action 3
    d=(d-1)%4
    while board[y+dy[d]][x+dx[d]] != 0:
        d=(d-1)%4
    x+=dx[d]
    y+=dy[d]

from pprint import pprint
print(answer)