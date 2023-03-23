import sys
input = sys.stdin.readline

from collections import deque
def bfs(i, graph, visited):
    q = deque()
    q.append(i)
    while q:
        now = q.popleft()
        if visited[now-1]:
            continue
        visited[now-1] = True
        for x in graph[now]:
            q.append(x)

def solution(graph):
    answer = 0
    visited = [False] * len(graph)
    for i in graph:
        if visited[i-1]:
            continue
        bfs(i, graph, visited)
        answer += 1
    return answer

N, M = map(int, input().split())
graph = {x: [] for x in range(1, N+1)}
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(solution(graph))