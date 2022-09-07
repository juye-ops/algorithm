def solution(n):
    answer = 0
    a = b = 0
    tmp = 0
    while a < n:
        if tmp <= n:
            b+=1
            tmp+=b
        elif tmp > n:
            a+=1
            tmp-=a
        if tmp == n:
            answer+=1

    return answer