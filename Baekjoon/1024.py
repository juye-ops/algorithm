def solution(N, L):
    while L <= 100:
        start = N - (L * (L+1))//2
        
        if start % L == 0:
            start = start//L
            
            if start >= -1:
                return " ".join([str(start+x) for x in range(1, L+1)])
                
        L+=1
    else:
        return -1

N, L = map(int, input().split())

print(solution(N, L))

# 등차수열
## L`(L`+1)/2 = 1 + 2 + 3 + 4 + ... + L`
## x + L`(L`+1)/2 = x + x+1 + x+2 + x+3 + ... + L`+x(개수가 L``)
### x = 임의의 시작 수

# N = L`x + L`(L`+1)/2 (L`은 주어진 L보다 크고, 수식을 만족하는 최소 자연수)