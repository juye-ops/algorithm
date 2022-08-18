def solution(n):
    a = [1,2,4]
    newa = []
    cnt = 0
    squarelist = []
    mm = 1
    while 3**mm < 500000000:
        squarelist.append(3**mm)
        mm+=1

    for i in squarelist:
        if i<n:
            n-=i
            cnt += 1

    n-=1
    for i in range(cnt+1):
        newa.append(a[(n%3)])
        n//=3
    realsum = 0
    for i in range(len(newa)):
        realsum+= newa[i] * (10**i)


    return str(realsum)