N = int(input())
A = map(int, input().split())
B, C = map(int, input().split())

answer = 0
for i in A:
    i-=B
    answer += 1
    if i <= 0:
        continue
    a, b = divmod(i, C)
    answer += a
    answer += bool(b)
print(answer)