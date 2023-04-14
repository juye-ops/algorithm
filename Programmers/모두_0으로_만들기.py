import sys
sys.setrecursionlimit(10 ** 6)

answer = 0

def dfs(graph, n, a, visited):
    global answer
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            a[n] += dfs(graph, i, a, visited)
            trig = False
    answer += abs(a[n])
    return a[n]

def solution(a, edges):
    if sum(a):
        return -1
    
    graph = {x:[] for x in range(len(a))}
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    
    visited = [False for _ in range(len(a))]
    dfs(graph, 0, a, visited)
    
    return answer