import heapq

def dijkstra(N, road, s):
    q = []
    distance = [int(1e9)] * (N + 1)

    # 작은 것만 계속 고려
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in road[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


def solution(N, M, X, road):
    default = dijkstra(N, road, X)
    distances = [dijkstra(N, road, x)[X] + default[x] for x in range(N)]
    
    return max(distances)
    
    

N, M, X = map(int, input().split())
road = {x:[] for x in range(N)}

for i in range(M):
    a, b, t = map(int, input().split())
    road[a-1].append((b-1, t))

print(solution(N, M, X-1, road))