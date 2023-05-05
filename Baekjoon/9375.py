from math import prod
from itertools import combinations

def solution(clothes):
    answer = 0
    return prod(map(lambda x: len(x) + 1, clothes.values())) - 1

for _ in range(int(input())):
    answer = 1
    clothes = {}
    for _ in range(int(input())):
        c, t = input().split()
        if clothes.get(t) is None:
            clothes[t] = []
        clothes[t].append(c)
    
    print(solution(clothes))