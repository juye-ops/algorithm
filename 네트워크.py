from collections import deque

def bfs(n, network, visited):
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if visited[now]:
            continue
        visited[now] = True
        for i in network[now]:
            q.append(i)

def solution(n, computers):
    networks = {x:[] for x in range(n)}
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j]:
                if j not in networks[i]:
                    networks[i].append(j)
                    networks[j].append(i)
    for i in range(n):
        if visited[i]:
            continue
        bfs(i, networks, visited)
        answer+=1
        
    return answer