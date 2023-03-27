def solution(a, b):
    primes = [True] * 1000001
    primes[0] = False
    primes[1] = False
    
    for i in range(2, b+1):
        if not primes[i]:
            continue
        if i >= a:
            print(i)
        for j in range(2*i, b+1, i):
            primes[j] = False
            

a, b = map(int, input().split())
solution(a, b)