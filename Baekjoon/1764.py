N, M = map(int, input().split())

unheard = set()
unseen = set()

for i in range(N):
    unheard.add(input())
for i in range(M):
    unseen.add(input())

unknown = unheard.intersection(unseen)
print(len(unknown))
print("\n".join(sorted(unknown)))