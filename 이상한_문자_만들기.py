def solution(s):
    answer = ''
    s = s.split(" ")
    length = len(s)
    cnt = 0
    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                answer+=i[j].upper()
            elif j % 2 == 1:
                answer+=i[j].lower()
        cnt+=1
        if cnt<length:
            answer+=" "
    return answer
