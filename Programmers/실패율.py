from collections import Counter

def solution(N, stages):
    answer = []
    people = len(stages)
    stg = dict(sorted(Counter(stages).items()))
    for i in range(1, N+1):
        if people == 0:
            answer.append((i, 0))
            continue
        if stg.get(i) == None:
            stg[i] = 0
        answer.append((i, stg[i]/people))
        people-=stg[i]

    answer,_ = zip(*sorted(answer, reverse=True, key= lambda x: (x[1], -x[0])))

    return answer