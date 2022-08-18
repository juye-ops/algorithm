from collections import deque


def toarray(puzzle):
    xmin = min(puzzle, key=lambda x: x[0])[0]
    ymin = min(puzzle, key=lambda x: x[1])[1]
    xmax = max(puzzle, key=lambda x: x[0])[0]
    ymax = max(puzzle, key=lambda x: x[1])[1]

    puzzle = list(map(lambda x: (x[0] - xmin, x[1] - ymin), puzzle))

    arr = [[0 for x in range(xmin, xmax + 1)] for y in range(ymin, ymax + 1)]
    for i in puzzle:
        x, y = i
        arr[y][x] = 1
    return arr


def rotate(puzzle):
    return [[x[y] for x in puzzle] for y in range(len(puzzle[0]) - 1, -1, -1)]


def bfs(game_board, xy, visited, trig):
    q = deque()
    width = len(game_board) - 1
    q.append(xy)
    empty = []
    while q:
        now = q.popleft()
        empty.append(now)
        x, y = now
        visited[y][x] = True

        if y > 0 and game_board[y - 1][x] == trig and not visited[y - 1][x]:
            q.append((x, y - 1))

        if y < width and game_board[y + 1][x] == trig and not visited[y + 1][x]:
            q.append((x, y + 1))

        if x > 0 and game_board[y][x - 1] == trig and not visited[y][x - 1]:
            q.append((x - 1, y))

        if x < width and game_board[y][x + 1] == trig and not visited[y][x + 1]:
            q.append((x + 1, y))

    return toarray(empty)

def countOne(puzzle):
    cnt = 0
    for i in puzzle:
        for j in i:
            cnt+=j
    return cnt

def solution(game_board, table):
    visited = [[False for _ in game_board] for _ in game_board]
    table_visited = [[False for _ in game_board] for _ in game_board]
    tables = []
    answer = 0
    for y in range(len(game_board)):
        for x in range(len(game_board)):
            if table[y][x] == 1 and not table_visited[y][x]:
                tables.append(bfs(table, (x, y), table_visited, 1))

    for y in range(len(game_board)):
        for x in range(len(game_board)):
            trig=False
            if game_board[y][x] == 0 and not visited[y][x]:
                map = bfs(game_board, (x, y), visited, 0)
                for i in tables:
                    tab = i
                    for j in range(4):
                        if not map == tab:
                            tab = rotate(tab)
                        else:
                            tables.remove(i)
                            trig = True
                            answer += countOne(i)
                            break
                    if trig: break

    return answer