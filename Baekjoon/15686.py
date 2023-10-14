from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
distance = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((j,i))
        elif board[i][j] == 2:
            chicken.append((j,i))

# 도시의 치킨 거리 도출
def city_distance():
    for i in chicken:
        cx, cy = i
        house_to_chicken = []
        for j in house:
            hx, hy = j
            d = abs(hx - cx) + abs(hy-cy)
            house_to_chicken.append(d)
        distance.append(house_to_chicken)

city_distance()
answer = 1e9
for i in combinations(distance, M):
    ans = 0
    for j in zip(*i):
        ans += min(j)
    answer = min(answer, ans)
print(answer)