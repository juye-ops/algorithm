def solution(answers):
    per1 = [1, 2, 3, 4, 5]
    per2 = [2, 1, 2, 3, 2, 4, 2, 5]
    per3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):
        if per1[i % 5] == answers[i]:
            correct[1] += 1
        if per2[i % 8] == answers[i]:
            correct[2] += 1
        if per3[i % 10] == answers[i]:
            correct[3] += 1

    sum_val = max(correct.values())
    return list(filter(lambda x: correct[x] == sum_val, correct.keys()))
