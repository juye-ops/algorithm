input()

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

print(sum(map(lambda x: x[0] * x[1], zip(A, B))))