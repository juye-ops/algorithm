def solution(a, b, n):
    answer = 0
    c = 0
    while n:
        n, r = divmod(n, a)
        c += r
        if c >= a:
            c -= a
            n+=1
        n *= b
        answer += n

    return answer