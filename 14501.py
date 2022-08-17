def solution(n):
    TP = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n+1)
    for i in range(len(TP)-1, -1, -1):
        T, P = TP[i]
        if T + i > n:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+T] + P, P, dp[i+1])
    print(max(dp))

solution(int(input()))