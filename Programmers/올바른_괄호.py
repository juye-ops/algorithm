def solution(s):
    if len(s) > 100000: return False

    cnt = 0
    for i in s:
        if i == "(": cnt += 1
        else: cnt -= 1

        if cnt < 0: return False

    if cnt == 0:return True
    else: return False