from itertools import combinations

def setZeroBase(arr_2d):
    x = min(arr_2d, key=lambda x: x[0])[0]
    y = min(arr_2d, key=lambda x: x[1])[1]
    return list(map(lambda a: (int(a[0] - x), int(a[1] - y)), arr_2d))

def cross(fx, fy):
    A, B, E = fx
    C, D, F = fy
    if A*D - B*C == 0:
        return
    x = (B*F - E*D) / (A*D - B*C)
    y = (E*C - A*F) / (A*D - B*C)
    if x.is_integer() and y.is_integer():
        return int(x), int(y)

def solution(line):
    
    xy = []
    comb = list(combinations(line, 2))
    for i in comb:
        a = cross(i[0], i[1])
        if a:
            xy.append(a)
    stars = setZeroBase(xy)
    
    x = max(stars, key=lambda x: x[0])[0]
    y = max(stars, key=lambda x: x[1])[1]
    answer = [["." for _ in range(x+1)] for a in range(y+1)]
    for i, j in stars:
        answer[j][i] = "*"
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    
    return list(reversed(answer))