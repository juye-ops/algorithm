def solution(dartResult):
    answer = 0
    score, bonus, option = [], [], []
    prev = ""
    for i in dartResult:
        if i.isdigit():
            if prev.isdigit():
                score[-1] = 10
                continue
            elif prev and prev.isalpha():
                option.append(1)
            score.append(int(i))

        elif i.isalpha():
            tmp = ""

            if i == "S":
                bonus.append(1)
            elif i == "D":
                bonus.append(2)
            elif i == "T":
                bonus.append(3)
        
        else:
            if i == "*":
                if len(option):
                    option[-1] *= 2
                option.append(2)
            elif i == "#":
                option.append(-1)
        
        prev = i

    if prev.isalpha():
        option.append(1)
    answer = 0
    for s,b,o in zip(score, bonus, option):
        answer += (s**b)*o
        


    return answer