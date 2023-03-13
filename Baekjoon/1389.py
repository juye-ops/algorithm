from collections import deque

def solution(N, M, graph):
    kevin = {}
    for i in range(1, N+1):
        visited = [0 for _ in range(1, N+1)]
        q = deque()
        q.append((i, 0))

        while q:
            now, cost = q.popleft()
            if visited[now-1]:
                continue
            visited[now-1] = cost

            for n in graph[now]:
                if not visited[n-1]:
                    q.append((n, cost+1))
        kevin[i] = sum(visited[:i-1] + visited[i:])
    answer = 1
    tmp = kevin[1]
    for i in kevin:
        if kevin[i] < tmp:
            answer = i
            tmp = kevin[i]
    return answer


N, M = map(int, input().split())
graph = {x: [] for x in range(1, N+1)}
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


print(solution(N, M, graph))

