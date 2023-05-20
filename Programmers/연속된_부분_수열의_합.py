def solution(sequence, k):
    answer = []
    p1 = p2 = 0
    
    target = sequence[0]
    
    while p2 < len(sequence):
        if target < k:
            p2 += 1
            if p2 < len(sequence):
                target += sequence[p2]
        elif target > k:
            target -= sequence[p1]
            p1 += 1
        elif target == k:
            if not answer:
                answer = [p1, p2]
            elif p2 - p1 < answer[1] - answer[0]:
                answer = [p1, p2]
            target -= sequence[p1]
            p1 += 1
    return answer