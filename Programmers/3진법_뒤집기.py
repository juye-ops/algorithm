def solution(n):
    ret = ""
    answer = 0
    while n > 0:
        n, r = divmod(n, 3)
        ret+=str(r)
    for i in range(len(ret)):
        answer+=int(ret[len(ret)-1-i]) * (3**i)

    return answer