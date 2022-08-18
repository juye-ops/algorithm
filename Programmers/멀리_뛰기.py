def fac(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def solution(n):
    answer = 0
    ary = []

    for i in range(int(n / 2)):
        ary.append(2)
    if (n % 2 == 1):
        ary.append(1)

    while 2 in ary:
        answer += fac(len(ary)) // fac(ary.count(2)) // fac(ary.count(1))
        ary.remove(2)
        ary.extend([1, 1])

    if (len(ary) != 0):
        answer += 1

    return answer%1234567