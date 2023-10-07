import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

clouds = [
    (N-2, 0),
    (N-2, 1),
    (N-1, 0),
    (N-1, 1)
]

for _ in range(M):
    delta, distance = map(int, input().split())
    moved_clouds = []
    # seq1,2
    for y, x in clouds:
        ny = (y + dy[delta-1]*distance)%N
        nx = (x + dx[delta-1]*distance)%N
        mc = (ny, nx)
        moved_clouds.append(mc)
        board[ny][nx] += 1
    # seq4
    for y, x in moved_clouds:
        basket = 0
        for d in range(1, 8, 2):
            if 0 <= y+dy[d] < N and 0 <= x+dx[d] < N:
                basket += bool(board[y+dy[d]][x+dx[d]])
        board[y][x] += basket

    # seq3,5
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if (i, j) not in moved_clouds and board[i][j] >= 2:
                board[i][j] -= 2
                new_clouds.append((i, j))
        
    clouds = new_clouds

print(sum(sum(board, [])))