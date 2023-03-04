def solution(N, words):
    answers = {}
    words.sort()
    for i in words:
        answers[i] = 0
        for j in answers:
            if i == j:
                continue
            if i.startswith(j):
                answers[j] += 1
                
    return list(answers.values()).count(0)

N = int(input())
words = [input() for _ in range(N)]

print(solution(N, words))