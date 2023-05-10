answer = 0
def dfs(graph, n, del_node):
    global answer
    if n == del_node:
        return
    if (not graph[n]) or graph[n] == [del_node]:
        answer += 1
        return 

    for i in graph[n]:
        dfs(graph, i, del_node)

def solution(N, tree, del_node):
    global answer
    graph = {x: [] for x in range(N)}
    start = None
    for i, n in enumerate(tree):
        if n == -1:
            start = i
        else:
            graph[n].append(i)
    dfs(graph, start, del_node)
    return answer


N = int(input())
tree = list(map(int, input().split()))
del_node = int(input())

print(solution(N, tree, del_node))