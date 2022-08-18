stairs = [int(input()) for x in range(int(input()))]
dp = [0] * len(stairs)
dp[0] = stairs[0]
if len(stairs)>1:
    dp[1] = stairs[0]+stairs[1]
    for i in range(2, len(stairs)):
        dp[i] = max(dp[i-3] + stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
print(dp[-1])