def solution(n, lost, reserve):
    used = set()
    lost.sort()
    for i in lost:
        if i in reserve:
            used.add(i)
        elif (i - 1 in reserve) and (i - 1 not in used):
            used.add(i - 1)
        elif (i + 1 in reserve) and (i + 1 not in used):
            used.add(i + 1)

    return n - len(lost) + len(used)