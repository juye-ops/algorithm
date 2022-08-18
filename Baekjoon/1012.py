from collections import deque

def bfs(farm, x, y):
    queue = deque([(x, y)])

    while queue:
        coord = queue.pop()
        farm[coord[1]][coord[0]] = 0

        if coord[0] > 0:
            if farm[coord[1]][coord[0] - 1]:
                queue.append((coord[0] - 1, coord[1]))
        if coord[0] < X-1:
            if farm[coord[1]][coord[0] + 1]:
                queue.append((coord[0] + 1, coord[1]))
        if coord[1] > 0:
            if farm[coord[1] - 1][coord[0]]:
                queue.append((coord[0], coord[1] - 1))
        if coord[1] < Y-1:
            if farm[coord[1] + 1][coord[0]]:
                queue.append((coord[0], coord[1] + 1))



for i in range(int(input())):
    X, Y, cab = list(map(int, input().split()))
    bug = 0
    farm = [[0 for _ in range(X)] for _ in range(Y)]

    for j in range(cab):
        cab_x, cab_y = list(map(int, input().split()))
        farm[cab_y][cab_x]=1
    for x in range(X):
        for y in range(Y):
            if farm[y][x] == 1:
                bug += 1
                bfs(farm, x, y)
    print(bug)