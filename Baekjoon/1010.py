from math import comb

for i in range(int(input())):
    a, b = list(map(int, input().split()))
    print(comb(b, a))