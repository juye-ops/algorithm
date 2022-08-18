input()
permute = list(map(int, input().split()))

answer = [-1 for _ in permute]

while min(permute)!=3000:
    a = permute.index(min(permute))
    answer[a] = max(answer)+1
    permute[a] = 3000
print(" ".join(list(map(str, answer))))