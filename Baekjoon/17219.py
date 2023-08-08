import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
memo = dict([input().split() for _ in range(N)])

for i in range(M):
    print(memo[input().strip()])