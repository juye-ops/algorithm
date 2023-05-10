from collections import Counter

def solution(k, tangerine):
    answer = 0
    for _, v in sorted(Counter(tangerine).items(), key=lambda x: x[1], reverse=True):
        if k <= 0:
            break
            
        k -= v
        answer += 1
    return answer