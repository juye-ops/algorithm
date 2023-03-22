import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def solution(N, queries):
    heap = []
    
    for i in queries:
        if i:
            heappush(heap, (abs(i), i))
        else:
            target = 0
            if heap:
                target = heappop(heap)[1]
            print(target)
    
N = int(input())
queries = [int(input()) for _ in range(N)]

solution(N, queries)