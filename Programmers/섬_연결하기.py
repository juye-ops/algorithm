# Union & Find Kruskal

def find(nodes, n):
    if nodes[n] == n:
        return n
    return find(nodes, nodes[n])
    
def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    nodes = [x for x in range(n)]
            
    answer = 0
    
    for a, b, cost in costs:
        if find(nodes, a) != find(nodes, b):
            nodes[find(nodes, a)] = find(nodes, b)
            answer += cost
            print(a, b, cost, nodes)
    return answer