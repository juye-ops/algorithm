def solution(m, n, puddles):
    answer = 0
    maps = [[0 for _ in range(m)]for _ in range(n)]
    for i in puddles:
        x, y = i[0]-1, i[1]-1
        maps[y][x] = -1

    for i in range(m):
        if maps[0][i] == -1:
            break
        maps[0][i] = 1

    for i in range(n):
        if maps[i][0] == -1:
            break
        maps[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if maps[i][j] == -1:
                continue
            a, b = maps[i-1][j], maps[i][j-1]
            if a == -1: a = 0
            if b == -1: b = 0
            maps[i][j] = a + b
    return maps[n-1][m-1]%1000000007

print(solution(4, 3, [[2,2]]))