import itertools
import math

def solution(clothes):
    dct = dict()
    for i in clothes:
        if i[1] not in dct:
            dct[i[1]] = 1
        else:
            dct[i[1]]+=1

    tmp = list(reversed(dct.values()))
    trig = False
    for i in tmp:
        if i != 1:
            trig = True
            break

    if not trig: return 2**len(dct) - 1


    answer = 0
    for i in range(len(dct)):
        permute = list(itertools.combinations(dct.values(), i+1))
        for j in permute:
            answer += math.prod(j)

    return answer