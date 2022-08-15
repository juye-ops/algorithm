def solution(num):
    for i in range(500):
        if num == 1: return i
        num = num/2 if not num%2 else num*3 + 1
    return -1