def dfs(n, network, visited):
    visited[n-1] = True
    if not network[n]:
        return
    while(network[n]):
        next = network[n].pop(0)
        network[next].remove(n)
        dfs(next, network, visited)


def solution(V, E):
    network = {x:[] for x in range(1, V+1)}
    visited = [False] * (V+1)
    for i in range(E):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)
    dfs(1, network, visited)
    return sum(visited[1:])


print(solution(int(input()), int(input())))