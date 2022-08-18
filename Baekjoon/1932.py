triangle = [list(map(int, input().split())) for i in range(int(input()))]

for i in range(1, len(triangle)):
    for j in range(i+1):
            triangle[i][j] += max(triangle[i-1][j] if j != i else 0, triangle[i-1][j-1] if j != 0 else 0)

print(max(triangle[-1]))