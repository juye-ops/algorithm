def solution(queue1, queue2):
    answer = 0
    queue = queue1+queue2
    p1 = 0
    p2 = len(queue1)
    sum_a = sum(queue1)
    sum_b = sum(queue2)
    while p2 < len(queue):
        if sum_a < sum_b:
            sum_a += queue[p2]
            sum_b -= queue[p2]
            p2+=1
            answer += 1
        elif sum_a > sum_b:
            sum_a -= queue[p1]
            sum_b += queue[p1]
            p1+=1
            answer += 1
        elif sum_a == sum_b:
            return answer
    return -1