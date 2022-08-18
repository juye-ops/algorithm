n = int(input())


for i in range(n+1):

    if i + sum(map(int, list(str(i))))== n:

        print(i)

        break

    if i == n:

        print(0)

