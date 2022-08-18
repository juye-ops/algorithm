import math

def solution(arr):
    answer = 1

    for i in arr:
        answer = answer * i // math.gcd(answer, i)

    return answer