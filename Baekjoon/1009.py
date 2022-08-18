for i in range(int(input())):
    a, b = list(map(int, input().split()))
    lst = []

    j = 1
    while True:
        if a%10 == 0:
            lst.append(10)
            break
        if b == 0:
            lst.append(1)
            break
        alpha = a ** j % 10
        if alpha not in lst:
            lst.append(alpha)
        else: break

        j+=1
    print(lst[b % len(lst) - 1])