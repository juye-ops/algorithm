from collections import deque


def bfs(graph, visited):
    q = deque()
    q.append((1, 1))
    while q:
        now, dis = q.popleft()
        if visited[now]:
            continue

        for i in graph[now]:
            q.append((i, dis+1))
        visited[now]=dis


def solution(n, edge):
    graph = {x: [] for x in range(1, n+1)}
    visited = {x:0 for x in range(1, n+1)}

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    bfs(graph, visited)
    return list(visited.values()).count(max(visited.values()))
