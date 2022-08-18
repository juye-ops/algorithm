for i in range(int(input())):
    value = 0
    sx, sy, ex, ey  = list(map(int, input().split(" ")))

    for j in range(int(input())):
        x, y, r = list(map(int, input().split()))
        s = (x - sx)**2 + (y - sy)**2
        e = (x - ex)**2 + (y - ey)**2
        r2 = r**2
        value += (int(s<r2) + int(e<r2)) % 2
    print(value)