from collections import deque

def solution(N, K):
    q = deque()
    q.append((N, 0))
    visited = [0] * 100001
    while q:
        now, answer = q.popleft()
        if now == K:
            break
        if visited[now] and now != N:
            continue
        visited[now] = answer
        
        if 0 < now+1 <= 100000:
            q.append((now+1, answer+1))
        if 0 <= now-1 < 100000:
            q.append((now-1, answer+1))
        if 0 < now*2 <= 100000:
            q.append((now*2, answer+1))
    
    return answer


N, K = map(int, input().split())
print(solution(N, K))