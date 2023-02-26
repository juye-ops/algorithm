def solution(k, m, score):
    score.sort()
    return sum(score[len(score)%m::m] * m)