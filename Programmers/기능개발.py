def solution(progresses, speeds):
    answer = []
    while progresses:
        func = 0
        progresses = [x+y for x, y in zip(progresses, speeds)]
        while progresses and  progresses[0] >= 100:
            func+=1
            progresses.pop(0)
            speeds.pop(0)
        if func:
            answer.append(func)


    return answer