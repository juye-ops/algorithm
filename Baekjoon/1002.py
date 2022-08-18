lst = [list(map(int, input().split(" "))) for _ in range(int(input()))]

for i in lst:
    d = ((i[3] - i[0])**2 + (i[4] - i[1])**2)**.5


    if i[0:3] == i[3:6]: print(-1)
    elif d > i[2] + i[5] or d < abs(i[2] - i[5]):print(0)
    elif d == i[2] + i[5] or d == abs(i[2] - i[5]): print(1)
    elif d < i[2]+i[5]: print(2)
