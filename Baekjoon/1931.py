def solution(n):
    conferences = []
    answer = 0
    for i in range(n):
        conferences.append(tuple(map(int, input().split())))
    conferences.sort(key=lambda x: (x[1], x[0]))
    now = (0, 0)
    for i in range(len(conferences)):
        if conferences[i][0] < now[1]:
            continue
        else:
            now = conferences[i]
            answer+=1
    return answer

print(solution(int(input())))