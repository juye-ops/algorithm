arr = []

for i in range(int(input())):
    arr.append(int(input()))
dp = [0] * len(arr)

dp[0] = arr[0]
if len(arr) >= 2:
    dp[1] = arr[0] + arr[1]

    for i in range(2, len(arr)):
        dp[i] = max(arr[i]+dp[i-2], arr[i] + arr[i-1] + dp[i-3], dp[i-1])

print(max(dp))