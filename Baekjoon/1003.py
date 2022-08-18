for i in range(int(input())):
    n = int(input())
    f0 = [1, 0]
    f1 = [0, 1]
    if n == 0:
        f0 = list(map(str, f0))
        print(" ".join(f0))
        continue
    elif n == 1:
        f1 = list(map(str, f1))
        print(" ".join(f1))
        continue
    else:
        f2 = []
        for j in range(2, n+1):
            f2 = [x+y for x, y in zip(f0, f1)]
            f0 = f1
            f1 = f2
        f2 = list(map(str, f2))
        print(" ".join(f2))
        continue