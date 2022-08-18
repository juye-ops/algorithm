def solution(n):
    a=[0,1]
    for i in range(n):
        a[i%2] = a[0] + a[1]
    return a[0]%1000000007 if(n % 2 != 0)  else a[1]%1000000007