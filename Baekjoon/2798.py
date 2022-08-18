from itertools import combinations

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))
a = combinations(lst, 3)
a = sorted(list(map(sum, a)))
tmp = 0
for i in a:
    if i>M: break
    else: tmp = i

print(tmp)