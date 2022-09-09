def primes_of(n):
    ret = set()
    for i in range(1, int(n**0.5)+1):
        q, r = divmod(n, i)
        if r == 0:
            ret.add(q)
            ret.add(i)
    return ret

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if len(primes_of(i)) % 2:
            answer-=i
        else: answer += i
    return answer