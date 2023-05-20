def solution(r1, r2):
    answer = 0
    for x in range(r2):
        answer += int((r2**2 - x**2)**0.5)
    for x in range(r1):
        tmp = (r1**2 - x**2)**0.5
        val = 0
        if tmp.is_integer():
            val = int(tmp)-1
        else:
            val = int(tmp)
        answer -= val
    return answer * 4
