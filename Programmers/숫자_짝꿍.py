from collections import Counter

def solution(X, Y):
    X, Y = Counter(X), Counter(Y)
    answer = ""
    for i in X:
        if Y.get(i) is None:
            continue
        answer += i*min(X[i], Y[i])

    if not answer: return "-1"
    elif answer.count("0") == len(answer): return "0"

    return "".join(sorted(answer, reverse=True))