def dfs(N, V, graph, visited, answer = []):
    if visited[V]:
        return
    visited[V] = True
    answer.append(V)
    
    for v in graph[V]:
        dfs(N, v, graph, visited, answer)
    
    return " ".join(map(str, answer))

    

def bfs(N, V, graph, visited):
    from collections import deque
    q = deque()
    q.append(V)
    answer = []
    while q:
        now = q.popleft()
        if visited[now]:
            continue
        visited[now] = True
        answer.append(now)
        for v in graph[now]:
            q.append(v)
    
    return " ".join(map(str, answer))


N, M, V = map(int, input().split())
graph = {x: [] for x in range(1, N+1)}
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for x in graph:
    graph[x].sort()

print(dfs(N, V, graph, {x: False for x in graph}))
print(bfs(N, V, graph, {x: False for x in graph}))
