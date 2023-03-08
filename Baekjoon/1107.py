def solution(N, M, broken):
    n = N
    channel1 = channel2 = 100
    while n >= 0:
        for x in str(n):
            if int(x) in broken:
                break
        else:
            channel1 = n
            break
        n-=1
    
    n = N
    
    while n < 1000000:
        for x in str(n):
            if int(x) in broken:
                break
        else:
            channel2 = n
            break
        n+=1
    
    return min(len(str(channel1)) + abs(channel1-N), len(str(channel2)) + abs(channel2-N), abs(N-100))
    

N = int(input())
M = int(input())
broken = []
if M:
    broken = list(map(int, input().split()))

print(solution(N, M, broken))