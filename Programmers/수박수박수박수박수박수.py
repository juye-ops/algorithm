def solution(n):
    answer = ""
    i = 0
    while i < n:
        answer+="수" if i % 2 == 0 else "박"
        i+=1
    return answer