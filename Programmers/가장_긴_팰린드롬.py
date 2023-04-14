def solution(s):
    answer = 1
    for i in range(len(s)-1):
        l = i
        r = i
        
        while r < len(s) and s[r] == s[l]:
            r+=1
        r-=1
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        answer = max(answer, r-l-1)

    return answer
