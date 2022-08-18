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