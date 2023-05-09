def solution(N, graph):
    for k in range(N):
        for i in range(N):
            for j in range(N): 
                if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                    graph[i][j] = 1
    
    for i in graph:
        print(*i, sep=" ")

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

solution(N, graph)