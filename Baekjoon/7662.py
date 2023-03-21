import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def solution(Q, queries):
    min_heap = []   # 최소 힙
    max_heap = []   # 최대 힙
    
    visited = [False] * Q
    
    for i, (q, v) in enumerate(queries):
        v = int(v)
        if q == "I":
            heappush(min_heap, (-v, i))
            heappush(max_heap, (v, i))
            visited[i] = True
        
        elif q == "D":
            if v == 1:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    val, idx = heappop(min_heap)
                    visited[idx] = False
            if v == -1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    val, idx = heappop(max_heap)
                    visited[idx] = False
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)

    if not(min_heap and max_heap):
        return "EMPTY"
    
    answer_a = -min_heap[0][0]
    answer_b = max_heap[0][0]
    
    return f"{answer_a} {answer_b}"

T = int(input())
for i in range(T):
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    print(solution(Q, queries))