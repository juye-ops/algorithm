import sys
input = sys.stdin.readline

answer = 0
def dfs(now, tree, visited, distance = 0):
    global answer, n
    node, dis = now
    distance+=dis
    if dis:
        if len(tree[node]) == 1:
            if answer < distance:
                answer = distance
                n = node
            return
    visited[node-1] = True
    for i in tree[node]:
        n_node, n_dis = i
        if not visited[n_node-1]:
            dfs(i, tree, visited, distance)
        

def solution(V, tree):
    global answer, n
    visited = [False] * V
    dfs((1, 0), tree, visited)
    visited = [False] * V
    dfs((n, 0), tree, visited)
    return answer
    

V = int(input())
tree = {x:[] for x in range(1, V+1)}
for i in range(V):
    v, *ve = map(int, input().split())
    ve = ve[:-1]
    for j in zip(ve[::2], ve[1::2]):
        tree[v].append(j)
        
print(solution(V, tree))