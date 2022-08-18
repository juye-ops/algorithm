def solution(sizes):
    width = max(max(sizes, key=lambda x: x[0])[0], max(sizes, key=lambda x: x[1])[1])
    answer = 0
    for i in sizes:
            answer = max(answer, min(i))
    return width * answer