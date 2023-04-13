def solution(citations):
    citations.sort()
    answer = 0
    for i, x in enumerate(reversed(citations)):
        if i < x:
            answer = i+1
    return answer