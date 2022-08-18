def solution(citations):
    answer = 0
    citations.sort()
    print(citations)
    for i in range(len(citations)):
        if i+1 <= citations[len(citations)-i-1]:
            answer +=1
        else: return answer
    return answer