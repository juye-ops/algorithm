def solution(number, k):
    q = []
    for i in number:
        while k and q and q[-1] < i:
            q.pop(-1)
            k-=1
        q.append(i)
    for i in range(k):
        q.pop()

    answer= "".join(q)

    return answer