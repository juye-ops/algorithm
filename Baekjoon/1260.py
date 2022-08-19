import copy
from collections import deque
import sys
sys.setrecursionlimit(10**9)

def dfs(n, graph, answers):
    if n not in answers:
        answers.append(n)

    if not graph[n]:
        return

    while(graph[n]):
        next = graph[n].pop(0)
        graph[next].remove(n)
        dfs(next, graph, answers)

def bfs(start, graph, answers):
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if now not in answers:
            answers.append(now)
        while(graph[now]):
            q.append(graph[now].pop(0))


def solution(V, E, start):
    graph = {x:[] for x in range(1, V+1)}
    answers1 = []
    answers2 = []
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in graph:
        graph[i].sort()


    dfs(start, copy.deepcopy(graph), answers1)
    bfs(start, copy.deepcopy(graph), answers2)
    answer = ""
    answer+=" ".join(map(str, answers1))
    answer+="\n"
    answer+=" ".join(map(str, answers2))
    return answer

print(solution(*map(int, input().split())))

