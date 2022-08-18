a = 2
cnt = True
distance = [1, 2]

while distance[-1] < 2**31:
    distance.append(distance[-1] + a)
    cnt = not cnt
    if cnt: a += 1


for i in range(int(input())):
    x, y = list(map(int, input().split()))

    for i in range(len(distance)):
        if (y-x) <= distance[i]:
            print(i+1)
            break
