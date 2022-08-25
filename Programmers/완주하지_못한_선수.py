from collections import Counter


def solution(participant, completion):
    a = Counter(participant)
    for i in completion:
        a[i] -= 1
        if a[i] == 0:
            del a[i]

    return list(a.keys())[0]