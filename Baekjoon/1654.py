def solution(K, N, cables):
    l = 1
    r = max(cables)
    answer = 0
    while l <= r:
        mid = (l+r) // 2
        
        n_o_cables = sum([x//mid for x in cables])
        
        
        if n_o_cables < N:
            r = mid-1
        elif n_o_cables >= N:
            l = mid+1
            answer = mid
    
    return answer


K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

print(solution(K, N, cables))