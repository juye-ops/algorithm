from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for i in list(permutations(dungeons)):
        stamina = k
        cnt = 0
        for j in i:
            if stamina >= j[0]:
                stamina -= j[1]
                cnt+=1
        answer = max(answer, cnt)
    return answer
    