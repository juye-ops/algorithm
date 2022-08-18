homes = [list(map(int, input().split())) for _ in range(int(input()))]

for i in range(1, len(homes)):
    for j in range(3):
        tmp_homes = homes[i-1].copy()
        tmp_homes.pop(j)
        homes[i][j]+=min(tmp_homes)
print(min(homes[-1]))
