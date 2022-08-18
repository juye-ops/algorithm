X = int(input())
DP = [[X]]
i = 0
while True:
    DP.append([])

    SET = sum(DP[:i], [])
    for j in DP[i-1]:
        if j%3 == 0 and j//3 not in SET and j//3 not in DP[i]:
            DP[i].append(j//3)
        if j%2 == 0 and j//2 not in SET and j//2 not in DP[i]:
            DP[i].append(j//2)
        if j-1 not in SET and j-1 not in DP[i]:
            DP[i].append(j-1)
    if 1 in DP[i]:
        break
    i+=1
print(i)