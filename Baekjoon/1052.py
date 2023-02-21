def lt_2square(n):
    a = 0
    while 2**a < n:
        a+=1
    return 2 ** (a-1)

N, K = map(int, input().split())
    
while K > 1:
    N -= int(lt_2square(N))
    K -= 1

print(int(lt_2square(N) * 2 - N))