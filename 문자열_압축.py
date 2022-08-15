from collections import defaultdict

def solution(s):
    answers = defaultdict(lambda: "")

    for i in range(1, len(s)+1):
        tmp = s[:i]
        count = 0
        for j in range(0, len(s), i):
            if tmp == s[j:j+i]:
                count += 1
            elif tmp != s[j:j+i]:
                answers[i]+=(str(count)+tmp) if count>=2 else tmp
                tmp = s[j:j+i]
                count = 1
        answers[i] += (str(count) + tmp) if count >= 2 else s[j:]
    return min(map(len, answers.values()))