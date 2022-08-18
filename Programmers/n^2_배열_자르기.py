def solution(n, left, right):
    answer = []
    k=0
    for i in range(left, right+1):
        answer.append(max(divmod(i, n))+1)

    return answer