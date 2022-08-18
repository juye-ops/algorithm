def solution(priorities, location):
    idx = location
    cnt = 0
    while(priorities):
        if max(priorities) == priorities[0]:
            cnt += 1
            priorities.pop(0)
            if idx == 0: return cnt
        else:
            priorities.append(priorities.pop(0))

        if idx == 0:
            idx = len(priorities)-1
        else:
            idx -= 1