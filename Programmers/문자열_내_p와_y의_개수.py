def solution(s):
    x, y = 0, 0
    for i in s.lower():
        x = x + 1 if i == 'p' else x
        y = y + 1 if i == 'y' else y
    return x == y