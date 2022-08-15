def solution(land):
    for i in range(1, len(land)):
        # tmp1 = land[i - 1]
        for j in range(4):
            tmp2 = land[i-1].copy()
            tmp2.pop(j)
            land[i][j] += max(tmp2)
    return max(land[-1])