def solution(money):
    dp1 = [money[0], money[1], money[2] if len(money)==3 else money[0]+money[2]]
    dp2 = [0, money[1], max(money[1:3])]
    for i in range(3, len(money)):
        dp1.append(max(dp1[i-3:i-1])+money[i])
        dp2.append(max(dp2[i-3:i-1])+money[i])
    return max(max(dp1[:-1]), dp2[-1])