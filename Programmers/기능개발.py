from math import ceil

def solution(progresses, speeds):
    answer = []
    before = 0
    for p, s in zip(progresses, speeds):
        now = ceil((100-p)/s) # progresses(현재 완료된 정도) + speed * now(앞으로 할 것) > 100
        if before < now:
            before = now
            answer.append(0)
        answer[-1] += 1
            
        
    return answer