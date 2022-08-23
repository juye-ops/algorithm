def solution(rows, columns, queries):
    boards = [[columns * y + x + 1 for x in range(columns)] for y in range(rows)]
    answer = []
    for i in queries:
        y1, x1, y2, x2 = i
        tmp = boards[y1-1][x1-1]
        minimum = boards[y1-1][x1-1]
        for x in range(x1 - 1, x2):
            tmp, boards[y1 - 1][x] = boards[y1 - 1][x], tmp
            minimum = min([tmp, minimum])
        for y in range(y1, y2):
            minimum = min([tmp, minimum])
            tmp, boards[y][x2 - 1] = boards[y][x2 - 1], tmp

        for x in range(x2 - 2, x1 - 2, -1):
            minimum = min([tmp, minimum])
            tmp, boards[y2 - 1][x] = boards[y2 - 1][x], tmp

        for y in range(y2 - 2, y1 - 2, -1):
            minimum = min([tmp, minimum])
            tmp, boards[y][x1 - 1] = boards[y][x1 - 1], tmp

        answer.append(minimum)

    return answer