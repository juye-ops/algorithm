def solution(N):
    answers = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    
    while True:
        now = []
        last = answers[-1]
        if len(last) == 1:
            break
        
        for i in range(1, len(last)):
            now.append(sum(last[:i]))
        
        answers.append(now)

    tmp = 0
    for i, x in enumerate(answers):
        if sum(x) + tmp - 1 < N:
            tmp += sum(x)
        else: break
    else:
        return -1
    now = N - tmp
    
    answer = ""
    for i in range(i, -1, -1):
        a = 0
        for j in range(len(answers[i])):
            a+=answers[i][j]
            if a > now:
                break
        answer += str(i+j)
        now -= sum(answers[i][:j])
    return answer
        
    


N = int(input())
print(solution(N))

# 1자리
## 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 (개)

# 2자리
## 1, 2, 3, 4, 5, 6, 7, 8, 9 (개)

# 3자리
## 1, 3, 6, 10, 15, 21, 28, 36, 45 (개)

# 4자리
## 1, 4, 9, ...

# n자리는 각 n-1자리의 [0:k]의 합