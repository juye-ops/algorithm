# DFS
visited = dict()
count = 0
def dfs(graph, s):
    global visited, count
    visited[s] = True
    count+=1
        
    for i in graph[s]:
        graph[i].remove(s)
        dfs(graph, i)

        
def solution(n, wires):
    global visited, count
    answers = []
    
    for delete in range(len(wires)):
        visited = {x: False for x in range(1, n+1)}
        tmp_wires = wires.copy()
        where = tmp_wires.pop(delete) 
        cnt = 0
        graph = {x: [] for x in range(1, n+1)}
        
        for wire in tmp_wires:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
            
        for i in graph:
            if not visited[i]:
                dfs(graph, i)
                if cnt == 0:
                    answers.append(count)
                    cnt+=1
                elif cnt == 1:
                    answers[-1] = abs(answers[-1] - count)
                count = 0
    return min(answers)



# BFS
from collections import deque

def bfs(graph, n, visited):
    ret = 0
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if visited[now]:
            continue
        visited[now] = True
        ret +=1
        
        for i in graph[now]:
            q.append(i)
    return ret

def solution(n, wires):
    answers = []
    
    for w in range(len(wires)):
        answer = 0
        wire = wires[:w] + wires[w+1:]
        graph = {x: [] for x in range(n)}
        for i, j in wire:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
            
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                val = bfs(graph, i, visited)
                if answer:
                    answer -= val
                    answers.append(abs(answer))
                else:
                    answer += val
    
    return min(answers)