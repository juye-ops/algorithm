input()
arr = list(map(int, input().split()))
dp = [0] * len(arr)

for i in range(len(arr)):
    idx = -1
    for j in range(i):
        if arr[i] > arr[j] and dp[j] > dp[idx]:
                idx = j

    dp[i] = 1 if idx == -1 else dp[idx]+1

print(max(dp))