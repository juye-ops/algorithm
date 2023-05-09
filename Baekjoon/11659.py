import sys
from itertools import accumulate
 
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

accum = [0] + list(accumulate(nums))

for i in range(M):
    i, j = map(int, input().split())
    print(accum[j] - accum[i-1])